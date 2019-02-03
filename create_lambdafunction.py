import boto3
import sys
import time

# This Lambda function was designed to pull some code from a zip file location in a place of your choice. For my test, 
# I used the S3 script below: 
# import boto3
# def get_s3buckets():
#        s3Buckets = boto3.client('s3')
#        resource = s3Buckets.list_buckets()
#        for b in resource['Buckets']:
#            print(b['Name'])

# You can, of course, use this to create any Lambda function you would like though. Enjoy!


def create_lambdafunction(LambdafunctionName, iamRole, PythonfunctionName):
    filePath = input(
        'Please enter the location of the zip file where your Python code is for your Lambda function: ')
    lambdaCreation = boto3.client('lambda')
    resource = lambdaCreation.list_functions()
    for f in resource['Functions']:
        if LambdafunctionName in f['FunctionName']:
            print('Lambda function already exists')
            print('Closing in 5 seconds')
            time.sleep(5)
            exit()

        else:
            newLambda = lambdaCreation.create_function(
                FunctionName=LambdafunctionName,
                Runtime='python3.7',
                # The role is the IAM role you created that has access to kick off the Lambda Function. You need to put in the ARN
                Role=iamRole,
                Handler='{}.lambda_handler'.format(PythonfunctionName),
                # The code below is some sample code. This will pull all of your S3 bucket names
                Code={'ZipFile': open(filePath, 'rb').read(), },
                Description='Print out all S3 bucket names'
            )

            print(newLambda)


LambdafunctionName = sys.argv[1]
iamRole = sys.argv[2]
PythonfunctionName = sys.argv[3]

if __name__ == '__main__':
    create_lambdafunction(LambdafunctionName, iamRole, PythonfunctionName)
