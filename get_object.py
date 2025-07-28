import boto3

s3 = boto3.client('s3')

bucket = 'abdi-060325'
Key = 'test_text_string.txt'

response = s3.get_object(Bucket=bucket, Key=Key)

object_content = response['Body'].read()
content = object_content.decode('utf-8')

print(content)
