import boto3
import sys
import os

def new_iam_user(accessKey, secretKey, username):
    # Create connection to AWS API
    iam_user = boto3.client('iam',
                            aws_access_key_id=accessKey,
                            aws_secret_access_key=secretKey)

    try:
        # Try to create a new user
        new_user_create = iam_user.create_user(
            UserName=username
        )
        print(new_user_create)

    except:
        # Always remember the naming convention needed by IAM and to ensure your accesskey/secretkey is correct
        print(
            'No new user was created, please confirm your region, accesskey, and secretkey were correct and try again')
        exit()

    try:
        # For the user that you just created, this will give them programmatic access for AWS CLI
        new_user_access = iam_user.create_access_key(
            UserName=username
        )

        print(new_user_access)

    except:
        print(
            'Users access key was not created. Please confirm you have permissions to utilize programmatic access in AWS and try again')

accessKey = sys.argv[1]
secretKey = sys.argv[2]
username = sys.argv[3]

if __name__ == '__main__':
    new_iam_user(accessKey, secretKey, username)
else:
    print('please run this directly from the script or take out the __name__ == __main__ if statement if you would prefer to not run this script as main and import as a module')