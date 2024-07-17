import sys
import boto3
import boto3.resources

aws_access_key_id = sys.argv[1]
aws_secret_access_key = sys.argv[2]

instance_type = "t3.micro"
ami = "ami-0249211c9916306f8"
region = "eu-north-1"

# Initialize a session using credentials
ec2 = boto3.resource('ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

# Create EC2 client

response = ec2.create_instances(ImageId=ami,InstanceType=instance_type,MinCount=1,MaxCount=1)
print(response[0].id)