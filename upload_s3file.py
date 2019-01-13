import boto3
import sys
import os

def upload_s3file(accessKey, secretKey, bucketName, filepath, filename):
    # Confirm path specified exists
    check_path = os.path.exists(filepath)

    try:
        # if statement that if the path doesn't exist, prompt for a new one. If it does exist, continue with the upload
        if check_path == False:
            confirm_path = input("Path does not exist. Please enter a proper filepath: ")

            s3_upload = boto3.resource('s3',
                                        aws_access_key_id=accessKey,
                                        aws_secret_access_key=secretKey)

            s3_upload.meta.client.upload_file(confirm_path, bucketName, filename)

        elif check_path == True:
            # filepath is where the file currently exists on your machine/server. Filename is what you want it to be called when it is uploaded
            s3_upload = boto3.resource('s3',
                                    aws_access_key_id=accessKey,
                                    aws_secret_access_key=secretKey)

            s3_upload.meta.client.upload_file(filepath, bucketName, filename)
    
    except Exception as e:
        print(e)

accessKey = sys.argv[1]
secretKey = sys.argv[2]
bucketName = sys.argv[3]
filepath = sys.argv[4]
filename = sys.argv[5]

if __name__ == '__main__':
    upload_s3file(accessKey, secretKey, bucketName, filepath, filename)
