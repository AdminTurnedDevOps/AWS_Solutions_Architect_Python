import boto3
import sys
import logging

global action

def start_stop_terminate_ec2instance(region, accessKey, secretKey, instanceID):

    # This input will allow you to pick your action of what you want to do with your EC2 instance
    action = input('Please type: \none for start \ntwo for stop \nthree for terminate \n')
    
    # Connection to the EC2 API
    ec2 = boto3.client('ec2',
                        region_name = region,
                        aws_access_key_id = accessKey,
                        aws_secret_access_key = secretKey)

    # First if statement is to start the instance
    if 'one' in action:
        ec2.start_instances(InstanceIds=[instanceID])
        print('starting: ' + instanceID)

    # First elif is to stop the instance
    elif 'two' in action:
        ec2.stop_instances(InstanceIds=[instanceID])
        print('stopping: ' + instanceID)

    # Second elif is to terminate the instance
    elif 'three' in action:
        ec2.terminate_instances(InstanceIds=[instanceID])
        print('terminating: ' + instanceID)
    
    # Else is for if start, stop, or terminate was not selected
    else:
        logging.debug('Checking argument')
        logging.info('stop, start or restart were not used')
        logging.warning('Please choose \n1: Start\n2: Stop \n3: Terminate')


region = sys.argv[1]
accessKey = sys.argv[2]
secretKey = sys.argv[3]
instanceID = sys.argv[4]

start_stop_terminate_ec2instance(region, accessKey, secretKey, instanceID)