import sys
import boto3
import boto3.resources

aws_access_key_id = sys.argv[1]
aws_secret_access_key = sys.argv[2]
ec2_id = sys.argv[3]
region = "eu-north-1"

# Initialize a session using credentials
ec2 = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region).client('ec2')

# Create EC2 client

response = ec2.terminate_instances(InstanceIds=[ec2_id])