import boto3
import sys
import os
import time

global tableName

def new_dynamodb_table(tableName):

    new_table = boto3.client('dynamodb')
    get_existing_table = boto3.client('dynamodb')
    new_item = boto3.client('dynamodb')

    try: 
        def get_tables(tableName):
            table = get_existing_table.describe_table(
                TableName = sys.argv[1]
            )
        pass
        get_tables(tableName)
    except:
        print('The table does not exist. Moving on')
    
    new_table.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': sys.argv[1],
                'AttributeType': 'S'
            },
        ],
        TableName = sys.argv[1],
        KeySchema=[
            {
                'AttributeName': sys.argv[1],
                'KeyType': 'HASH',
            }
        ],
        ProvisionedThroughput= {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10,
        }
    )

    print('Creating Table. May take up to 20 seconds')
    time.sleep(20)
    print('Creation: Complete')

    newItem = input('Would you like to create a new item?: ')
    if 'Y' in newItem or 'Yes' in  newItem:
        value = input('Please enter a new item: ')
        new_table_item = new_item.put_item(
            TableName = sys.argv[1],
            Item={
                sys.argv[1]: {
                    'S': value
                }
            }
        )

    elif 'N' in newItem or 'No' in newItem:
        print('No new item. Exiting')

tableName = sys.argv[1]

if __name__ == '__main__':
    new_dynamodb_table(tableName)