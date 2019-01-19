import boto3
import sys
import logging

global action

def stoporstart_ec2instance(region, accessKey, secretKey, instanceID):

    action = input('Please type: \none for start \ntwo for stop \nthree for terminate \n')
    ec2 = boto3.client('ec2',
                        region_name = region,
                        aws_access_key_id = accessKey,
                        aws_secret_access_key = secretKey)

    if 'one' in action:
        ec2.start_instances(InstanceIds=[instanceID])
        print('starting: ' + instanceID)

    elif 'two' in action:
        ec2.stop_instances(InstanceIds=[instanceID])
        print('stopping: ' + instanceID)

    elif 'three' in action:
        ec2.terminate_instances(InstanceIds=[instanceID])
        print('terminating: ' + instanceID)
    
    else:
        logging.debug('Checking argument')
        logging.info('stop, start or restart were not used')
        logging.warning('Please choose \n1: Start\n2: Stop')


region = sys.argv[1]
accessKey = sys.argv[2]
secretKey = sys.argv[3]
instanceID = sys.argv[4]

stoporstart_ec2instance(region, accessKey, secretKey, instanceID)