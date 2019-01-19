import boto3
import sys
import logging
import time

def attach_ebsvolume(instanceID):
    
    try: 
        new_ebs = boto3.client('ec2')

        create = new_ebs.create_volume(
            AvailabilityZone=input('Please enter availability zone: '),
            Size=int(input('Pleae enter size: ')),
            VolumeType='gp2'
        )

        print('Pausing while the EBS volume creates')
        time.sleep(10)

        response = new_ebs.attach_volume(
            Device='/dev/sdf',
            InstanceId=instanceID,
            VolumeId=str(create['VolumeId']),
        )
        print(response)
    
    except Exception as e:        
        logging.debug('Checking resource')
        logging.info('an issue with the EC2 volume occured occured')
        logging.warning('EBS volume not created or EC2 instance does not exist')
        print(e)
    
instanceID = sys.argv[1]
attach_ebsvolume(instanceID)