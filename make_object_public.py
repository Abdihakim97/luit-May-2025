import boto3

s3 = boto3.client('s3')

Bucket="abdi-060325"
Key = "test_text_string.txt"

response = s3.put_public_access_block(
    Bucket=Bucket,


    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
    
)



response = s3.put_bucket_ownership_controls(
    Bucket=Bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    },
  
)


response = s3.put_bucket_acl(
    ACL='private',
    Bucket=Bucket,
    
)


response = s3.put_object_acl(ACL='public-read', 
                             Bucket=Bucket, 
                             Key=Key)


print(response)
