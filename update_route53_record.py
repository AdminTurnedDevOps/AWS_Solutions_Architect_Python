import boto3 as route53
import sys
import logging
import time

global dnsEntry

def update_route53_record(hostedZone, name, type, value):
    dnsEntry = route53.client('route53')
    print('Please use a hosted zone id for your hosted zone parameter')
    print('Please use an FQDN for your DNS host name. For example, foobar.example.com.')
    print('For type, please use one of the following: \nSOA \nA \nTXT \nNS \nCNAME \nMX \nNAPTR \nPTR \nSRV \nSPF')
    time.sleep(5)
    
    try:
        newEntry = dnsEntry.change_resource_record_sets(
            HostedZoneId = hostedZone,
            ChangeBatch={
                'Comment': 'Updating: {}'.format(name),
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': name,
                            'Type': type,
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': value
                                }
                                
                            ]
                        }
                    }
                ]
            }

        )

    except Exception as e:
        logging.warning('WARNING: An error has occured')
        print(e)

hostedZone = sys.argv[1]
name = sys.argv[2]
type = sys.argv[3]
value = sys.argv[4]

if __name__ == '__main__':
     update_route53_record(hostedZone, name, type, value)