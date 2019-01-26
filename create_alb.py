import boto3
import sys
import logging
import time

def create_alb(lbName, Scheme, LBtype):

    subnet1 = input('Please enter first subnet: ')
    subnet2 = input('Please enter second subnet: ')
    securityGroup = input('Please enter security group: ')

    lb = boto3.client('elbv2')
    new_lb = lb.create_load_balancer(
        Name=lbName,
        Subnets=[subnet1, subnet2],
        SecurityGroups=[securityGroup],
        Scheme=Scheme,
        Type=LBtype,
        IpAddressType='ipv4'

    )
    print(new_lb)

lbName = sys.argv[1]
Scheme = sys.argv[2]
LBtype = sys.argv[3]

if __name__ == '__main__':
    create_alb(lbName, Scheme, LBtype)
