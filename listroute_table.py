import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routeTable in response["RouteTables"]:

    print(routeTable["VpcId"], routeTable["RouteTableId"])


