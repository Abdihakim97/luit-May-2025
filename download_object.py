import boto3
import os
from list_objects import list_objects_Keys

def downlaod_single_object(client, bucket, Key, filename):

    client.download_file(bucket, Key, filename)

if __name__ == '__main__':

    bucket = 'abdi-060325'
    Key = 'test_text_string.txt'
    Filename = "test_text_string.txt"

    s3 = boto3.client('s3')

    keys = list_objects_Keys(s3, bucket)

    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass

        else: 
            downlaod_single_object(s3, bucket, Key, key)
        print(keys)