import boto3

# Replace with your AWS region
region_name = 'us-east-1'

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region_name)

# Create an S3 client
s3 = boto3.client('s3', region_name=region_name)


def list_ec2_instances():
    """Lists all EC2 instances."""
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")


def list_s3_buckets():
    """Lists all S3 buckets."""
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")


if __name__ == '__main__':
    print("Listing EC2 Instances:")
    list_ec2_instances()
    print("\nListing S3 Buckets:")
    list_s3_buckets()
