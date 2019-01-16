import boto3
import logging
import sys

def get_ec2_info(error_log_path):

    try: 
        ec2 = boto3.resource('ec2')
        print_instances = ec2.instances.all()
        
        print('Below are stats for each EC2 instance\n')
        for ec2instance in print_instances:
            print(
                "ID: {}\nType: {} \nPublic IPv4: {}\nAMI: {}\nState: {}\nTags: {}\nSecurityGroups: {}\n".format(
                    ec2instance.id,  ec2instance.instance_type, ec2instance.public_ip_address, ec2instance.image.id, ec2instance.state, ec2instance.tags, ec2instance.security_groups
                )
            )
    except Exception as e:
        logging.basicConfig(filename='{}'.format(error_log_path), level=logging.DEBUG)
        logging.debug('Checking resource')
        logging.info('an issue with the EC2 resource occured')
        logging.warning(e)
        print(e)

error_log_path = sys.argv[1]

if __name__ == '__main__':
    get_ec2_info(error_log_path)