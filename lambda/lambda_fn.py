import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    client = boto3.client("ec2")
    status = client.describe_instance_status(IncludeAllInstances = True)

    for i in status["InstanceStatuses"]:
        print("This is the Lambda function from Lab 1 - an EC2 instance has just started running!")
        print("AvailabilityZone :", i["AvailabilityZone"])
        print("InstanceId :", i["InstanceId"])
        print("InstanceState :", i["InstanceState"])
        print("InstanceStatus", i["InstanceStatus"])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
