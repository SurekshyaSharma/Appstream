import csv
import boto3 
import pytz
import time
from datetime import datetime, timedelta
# current_time = int(datetime.now())
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    current_date = datetime.now(pytz.timezone('US/Central'))
    yesterday_date = current_date - timedleta(days=1)
    yesterday_date_string = yesterday_date.strftime("%Y-%m-%dT")

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('AppStreamDynamoDB1')


    response = table.scan(
        FilterExpression=Attr('formData').contains(yesterday_date_string)
    )
    items = response['Items']
    print(items)  # it should print out the values
    print("testing")
    print(yesterday_date_string)

    if len(items) != 0:
        print(items)  # it should print null
    return items

  
    saving_backup()
    delete_entires()

def saving_backup():
    s3_client = boto3.client('s3')
    key = datetime.now(pytz.timezone('US/Central')).strftime("%Y-%m-%dT")
    bucket = 'REPLACE_WITH_BUCKET_NAME'
    data = []
    serializedData = json.dumps(data)
    try:
        # response = s3_client.upload_file(file_name, bucket, object_name)
        response = s3.put_object(Bucket=bucket, Key=key, Body=serializedData)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def delete_entires():
    saving_backup() == True
    #----------------------Delete Items inside the dynamo db---------------------------------------------

    print("Attempting a conditional delete...")

    try:
        response = table.delete_item(
            Key={
                'date': yesterday_date_string ,
                
            },
            # ConditionExpression="info.rating <= :val",
            # ExpressionAttributeValues= {
            #     ":val": decimal.Decimal(5)
            # }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("DeleteItem succeeded:")
        # print(json.dumps(response, indent=4, cls=DecimalEncoder))
