import base64
import sys
import boto3
import boto3.resources

aws_access_key_id = sys.argv[1]
aws_secret_access_key = sys.argv[2]
gh_token = sys.argv[3]

instance_type = "t3.micro"
ami = "ami-0249211c9916306f8"
region = "eu-north-1"

# Initialize a session using credentials
ec2 = boto3.resource('ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)


user_data_script = f'''#!/bin/bash

yum install docker

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
  apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


# Example user data script
mkdir actions-runner && cd actions-runner
export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
curl -o actions-runner-linux-x64-2.317.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz
echo "9e883d210df8c6028aff475475a457d380353f9d01877d51cc01a17b2a91161d  actions-runner-linux-x64-2.317.0.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.317.0.tar.gz
yum install libicu -y
RUNNER_ALLOW_RUNASROOT=true GITHUB_ACTIONS_RUNNER_HTTPTRACE=true ./config.sh --unattended --url https://github.com/AnatoliiYakubyshyn/SelenideGhActions --pat {gh_token}

RUNNER_ALLOW_RUNASROOT=true ./run.sh
'''
# Create EC2 client

response = ec2.create_instances(ImageId=ami,InstanceType=instance_type,MinCount=1,MaxCount=1,
                                UserData=base64.b64encode(user_data_script.encode("ascii")).decode('ascii'))
print(response[0].id)
sys.stdout.flush()