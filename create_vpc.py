import boto3
import sys

def create_VPC(cidr, amzIP6, tenancy):

    ec2 = boto3.resource('ec2')
    vpc = ec2.create_vpc(
                         CidrBlock=cidr,
                         AmazonProvidedIpv6CidrBlock=bool(amzIP6),
                         InstanceTenancy=tenancy
                        )
    return vpc

cidr = sys.argv[1]
amzIP6 = sys.argv[2]
tenancy = sys.argv[3]

print(create_VPC(cidr, amzIP6, tenancy))