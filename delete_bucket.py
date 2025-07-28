import boto3

s3 = boto3.client('s3')

bucket = "abdi-060325"

response = s3.delete_bucket(
    Bucket=bucket
)