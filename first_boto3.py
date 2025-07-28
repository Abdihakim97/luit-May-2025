import boto3

s3 = boto3.client('s3', region_name='us-east-1')

response = s3.create_bucket(
    Bucket='abdi-060325'
)

print(response)


