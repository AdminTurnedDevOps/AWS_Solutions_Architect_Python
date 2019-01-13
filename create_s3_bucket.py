import boto3
import sys

def create_bucket(region, accessKey, secretKey, bucketName):

    try:
        # Connect to the s3 API
        s3_bucket = boto3.client('s3',
                                region_name = region,
                                aws_access_key_id = accessKey,
                                aws_secret_access_key = secretKey)

        # Create a new bucket with the ACL as private and your specified bucket name
        new_bucket = s3_bucket.create_bucket(
            Bucket=bucketName,
            ACL = 'private',
        )
    
    except Exception as e:
        print(e)

region = sys.argv[1]
accessKey = sys.argv[2]
secretKey = sys.argv[3]
bucketName = sys.argv[4]

if __name__ == '__main__':
    create_bucket(region, accessKey, secretKey, bucketName)