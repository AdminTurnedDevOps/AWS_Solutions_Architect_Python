import boto3
import sys

def change_s3bucket_aclperms(region, accessKey, secretKey, bucketName, ACLPerms):
    # List which ACL options are available
    print('Please choose from the following ACL Perms: \t\nprivate \t\npublic-read \t\npublic-read-write \t\nauthenticated-read')

    try:
        # If statement that accepts only the following strings
        if 'private' or 'public-read' or 'public-read-write' or 'authenticated-read' in bucketName:
            # Connect to your specified bucket
            s3bucket_perms = boto3.resource('s3',
                                            region = region,
                                            aws_access_key_id=  accessKey,
                                            aws_secret_access_key = secretKey)

            bucket_perms = s3bucket_perms.BucketAcl(bucketName)
            
            # Call the ACL perms that you specified and attach them to your bucket
            new_perms = bucket_perms.put(
                ACL = ACLPerms
            )
        else:
            print('Invalid choice. Please choose from the list above.')

    except Exception as e:
        print(e)

region = sys.argv[1]
accessKey = sys.argv[2]
secretKey = sys.argv[3]
bucketName = sys.argv[4]
ACLPerms = sys.argv[5]

if __name__ == '__main__':
    change_s3bucket_aclperms(region, accessKey, secretKey, bucketName, ACLPerms)
