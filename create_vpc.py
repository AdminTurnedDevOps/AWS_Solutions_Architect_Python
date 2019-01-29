import boto3
import sys

ec2 = boto3.resource('ec2')

def create_VPC(cidr, tenancy, name):
    #Create vpc
    vpc = ec2.create_vpc(
                         CidrBlock=cidr,
                         AmazonProvidedIpv6CidrBlock=False,
                         InstanceTenancy=tenancy
                        )
    vpc.create_tags(
                    Tags=[{
                        "Key": "Name",
                        "Value": name
                    }])

    #Create subnet
    subnet = ec2.create_subnet(
                               CidrBlock='10.100.1.0/24',
                               VpcId=vpc.id
                              )
    subnet.create_tags(
        Tags=[{
            "Key": "Name",
            "Value": name
        }])

    #Create internet gateway
    igw = ec2.create_internet_gateway()
    igw.attach_to_vpc(
                      VpcId=vpc.id
                     )
    igw.create_tags(
        Tags=[{
            "Key": "Name",
            "Value": name
        }])

    return subnet
    return vpc
    return igw


cidr = sys.argv[1]
tenancy = sys.argv[2]
name = sys.argv[3]

print(create_VPC(cidr, tenancy, name))