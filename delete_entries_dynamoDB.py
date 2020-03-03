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

    table = dynamodb.Table('serverlessrepo-serverless-form-handler-FormDataTable-1UNKJ1074YHCK')


    response = table.scan(
        FilterExpression=Attr('formData').contains(yesterday_date_string)
    )
    items = response['Items']
    print(items)  # it should print out the values
    print(yesterday_date_string)

    if len(items) != 0:
        print(items)  # it should print null
    return items

    saving_backup()
    delete_entires()

def saving_backup():
    s3 = boto3.resource('s3')
    s3.Object('mybucket', 'Items_Copy.txt').put(Body=open('/tmp/Iems_Copy.txt', 'rb'))
    #   data = s3.get_object(Bucket='my_s3_bucket', Key='main.txt')
    # contents = data['Body'].read()
    # print(contents)
    # ---------------------Reading and -Writing the file in S3 bucket-------------------------------------
    with open('Items_Copy.txt', 'w') as f:
        csv.writer(f, delimiter=' ').writerows(items)


def delete_entires():
    saving_backup() == True
    #----------------------Delete Items inside the dynamo db---------------------------------------------
    del items[:]
