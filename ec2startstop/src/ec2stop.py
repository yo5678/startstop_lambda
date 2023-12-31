import boto3
import instancesid as instancesid
from aws_lambda_powertools import Logger


logger = Logger()


def ec2_stop():
    ec2 = boto3.client("ec2")

    ec2.stop_instances(InstanceIds=instancesid.instances)
    logger.info("stopped your instances: " + str(instancesid.instances))

    return "stop_ec2"


def lambda_handler(event, context):
    ec2_stop()
