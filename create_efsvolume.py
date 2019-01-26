import boto3
import sys
import os
import random
import string

def generate_token(size=15, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    rando = ''.join(random.choice(chars) for _ in range(size))
    return rando

def check_ec2instance():
    print('Lets check if the EC2 instance exists that you are looking to mount')
    describe = input('Please enter instance id: ')
    
    check_ec2 = boto3.client('ec2')
    resource = check_ec2.describe_instances(InstanceIds=[describe])

    print(resource)

def create_filesystem():
    print('Creating file system\n')
    create_efs = boto3.client('efs')

    create_efs = create_efs.create_file_system(
        CreationToken=generate_token(),
        PerformanceMode='generalPurpose'
    )

    print(create_efs)

if __name__ == '__main__':
    check_ec2instance()
    create_filesystem()
