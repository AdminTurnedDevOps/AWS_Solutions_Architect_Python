import boto3
import sys

def new_redis_cluster(clusterID, instanceSize, cacheName):
    new_cluster = boto3.client('elasticache')
    new_cluster.create_cache_cluster(
        CacheClusterId = clusterID,
        AZMode='single-az',
        NumCacheNodes = 1,
        CacheNodeType = instanceSize,
        Engine='redis',
        Tags = [
            {
                'Key': 'Name',
                'Value': cacheName,
            },
        ]
    )
    print(cacheName + ' cluster: Created')

clusterID = sys.argv[1]
instanceSize = sys.argv[2]
cacheName = sys.argv[3]

if __name__ == '__main__':
    new_redis_cluster(clusterID, instanceSize, cacheName)