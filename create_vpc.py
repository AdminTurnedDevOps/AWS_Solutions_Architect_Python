import boto3
import sys
# To use this script supply cidr block, tenancy, name for vpc, and whether or not the subnet is public or private
# ex: create_vpc.py 10.100.100.0/16 default myName public

ec2 = boto3.resource('ec2')

def create_VPC(cidr, tenancy, name, privPub):
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

    #Create route-table and route to internet if VPC is public
    if privPub != 'public':
        pass
    else:
        rt_table = vpc.create_route_table()
        route = rt_table.create_route(
                                DestinationCidrBlock = '0.0.0.0/0',
                                GatewayId = igw.id
                            )

    return subnet
    return vpc
    return igw

cidr = sys.argv[1]
tenancy = sys.argv[2]
name = sys.argv[3]
privPub = sys.argv[4]

create_VPC(cidr, tenancy, name, privPub)
print('Your VPC is ready for usage')
