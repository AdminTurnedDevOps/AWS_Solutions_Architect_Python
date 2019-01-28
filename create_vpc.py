import boto3
import sys

ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(
                     CidrBlock='10.100.0.0/16',
                     AmazonProvidedIpv6CidrBlock=False,
                     InstanceTenancy='default'
)

print(vpc)