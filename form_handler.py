import boto3
from botocore.exceptions import ClientError
import json
import os
import time
import uuid
import decimal

dynamodb = boto3.resource('dynamodb')

def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Allow' : "OPTIONS, POST",
            'Access-Control-Allow-Headers': "Content-Type",
            'Access-Control-Allow-Methods': "OPTIONS,POST"
            }
        }

def lambda_handler(event, context):
    
    try:
        print(event)
    
        formData = json.loads(event['body'])
        timestamp = int(time.time() * 100)
        # Insert details into DynamoDB Table
        table = dynamodb.Table(os.environ['AppStreamTable'])
        item = {
            'Id': str(uuid.uuid1()),
            'facultyname': formData['facultyname'],
            'email': formData['email'],
            'department': formData['department'],
            'indexcode': formData['indexcode'],
            'starttime': formData['starttime'],
            'duration': formData['duration'],
            'image': formData['image'],
            'numberofinstances': formData['numberofinstances'],
            'createdAt': timestamp
        }
        table.put_item(Item=item)
        return response({'message': 'Big Thumbs up'}, 200)
    except Exception as e:
        return response({'message': 'Did not work'}, 400)
