import boto3

def filter_object_extension(client, bucket, extension):
    Keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if (extension in content["Key"][-(len(extension)):]):
            Keys.append(content["Key"])

    return Keys



def list_objects_Keys(client, bucket, prefix=""):
    Keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
        Keys.append(content["Key"])

    return Keys


if __name__ == '__main__':
    s3 = boto3.client('s3')

    response = list_objects_Keys(s3, "abdi-060325", "folder/")
    print(response)

    response = filter_object_extension(s3, "abdi-060325", "./")
    print(response)





