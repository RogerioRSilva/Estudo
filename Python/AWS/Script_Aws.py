# 1º - Criando instancias EC2

# 2º - Reduzindo o tamaho de imagens dentro do Amazon S3

# 3º - Backp programado de instancias EC2

# 4º - EC2 on e off (Ligar e desligar instancias)

# 5º - Backup das tabelas do DynamoDb

import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)