import boto3 as route53
import sys
import logging
import time

global dnsEntry

def create_route53_alias_record(hostedZone, name, aliasValue):
    dnsEntry = route53.client('route53')
    print('Please use a hosted zone id for your hosted zone parameter')
    print('Please use an FQDN for your DNS host name. For example, foobar.example.com.')
    time.sleep(5)

    try:
        newEntry = dnsEntry.change_resource_record_sets(
            HostedZoneId=hostedZone,
            ChangeBatch={
                'Comment': 'Creating: {}'.format(name),
                'Changes': [
                    {
                        'Action': 'CREATE',
                        'ResourceRecordSet': {
                            'Name': name,
                            'Type': 'CNAME',
                            'TTL': 300,

                            'ResourceRecords': [
                                {
                                    'Value': aliasValue
                                }
                            ],
                        }

                    }
                ]
            }

        )
        print(newEntry)

    except Exception as e:
        logging.warning('WARNING: An error has occured')
        print(e)


hostedZone = sys.argv[1]
name = sys.argv[2]
aliasValue = sys.argv[3]

if __name__ == '__main__':
    create_route53_alias_record(hostedZone, name, aliasValue)
