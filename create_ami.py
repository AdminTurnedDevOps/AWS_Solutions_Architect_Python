import boto3 as amicreation
import logging
import sys
import time

def create_ami(imageDescription, instanceID, imageName):

    try: 
        ami = amicreation.client('ec2')
        ami.create_image(
            Description = imageDescription,
            InstanceId=instanceID,
            Name=imageName,
            NoReboot=True
        )
    except:
        logging.debug('Checking instance ID and IAM credentials')
        logging.info('A valid instance Id or IAM credentials were not used')
        logging.warning('PLEASE USE A VALID INSTANCE ID AND IAM CREDENTIALS')

imageDescription = sys.argv[1]
instanceID = sys.argv[2]
imageName = sys.argv[3]

if __name__ == '__main__':
    print('Creating AMI: ' + imageName)
    create_ami(imageDescription, instanceID, imageName)

else:
    print('running as imported module')
    time.sleep(5)
    create_ami(imageDescription, instanceID, imageName)