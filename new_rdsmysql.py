import boto3
import sys
import time
import logging
import getpass

def new_rdsmysql(dbname, instanceID, storage, dbInstancetype, dbusername):
    
    masterPass = getpass.getpass('DBMasterPassword: ')
    if len(masterPass) < 10:
        logging.warning('Password is not at least 10 characters. Please try again')
        time.sleep(5)
        exit
    else:
        None
    
    try:
        rds_instance = boto3.client('rds')
        create_instance = rds_instance.create_db_instance(
            DBName = dbname,
            DBInstanceIdentifier = instanceID,
            AllocatedStorage = int(storage),
            DBInstanceClass = dbInstancetype,
            Engine = 'mysql',
            MasterUsername = dbusername,
            MasterUserPassword = str(masterPass),
            MultiAZ = True,
            EngineVersion = '5.7.23',
            AutoMinorVersionUpgrade = False,
            LicenseModel = 'general-public-license',
            PubliclyAccessible = False,

            Tags = [
                {
                'Key': 'Name',
                'Value' : dbname
                }
            ]
        )

        print(create_instance)
    except Exception as e:
        logging.warning('An error has occured')
        print(e)

dbname = sys.argv[1]
instanceID = sys.argv[2]
storage = sys.argv[3]
dbInstancetype = sys.argv[4]
dbusername = sys.argv[5]

new_rdsmysql(dbname, instanceID, storage, dbInstancetype, dbusername)