import json
import boto3
import os
# for timezone() 
import pytz 
import time
from datetime import datetime, timedelta
#current_time = int(datetime.now())
from boto3.dynamodb.conditions import Key, Attr
from urllib.parse import urlparse

#params_url = os.environ['paramsFile']
template_url = os.environ['templateUrl']

# def parse_params():
#   s3 = boto3.resource('s3')
#   s3_parse = urlparse(params_url)
#   bucket = s3_parse.netloc
#   s3_key = s3_parse.path.lstrip('/')
#   s3_obj = s3.Object(bucket, s3_key)
#   template_raw_data = s3_obj.get()["Body"].read().decode('utf-8')
#   template_params = json.loads(template_raw_data)
#   return template_params

def lambda_handler(event, context):

	#using now() to get current time 
	current_date = datetime.now(pytz.timezone('US/Central'))
	current_date_string = current_date.strftime("%Y-%m-%dT")

	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('serverlessrepo-serverless-form-handler-FormDataTable-JSOGC6VGOTQN')

	one_hour_ahead = current_date + timedelta(hours=1)
	one_hour_ahead_string = one_hour_ahead.strftime("%H:")

	response = table.scan(
		FilterExpression=Attr('formData').contains(current_date_string) & Attr('formData').contains(one_hour_ahead_string)
	)

	items = response['Items']
	print(items)
	print(current_date_string)
	print(one_hour_ahead_string)

	if len(items) != 0:
	  stack_result=launch_stack()
	  print(stack_result)

	  if stack_success(stack_result):
	   resp_txt = "Your stack has been launched. Please visit the AWS Console to track its progress"
	  else:
	   resp_txt = "Your stack failed to launch. Please visit the AWS Console to investigate further"

	  json_resp = {
		"version": "1.0",
    	"response": {
      	  "outputSpeech": {
			"type": "PlainText",
        	"text": resp_txt
      	  },
      	  "shouldEndSession": "true"
    	}
  	  }
	  return json_resp
		# invokeLam = boto3.client("lambda", region_name="us-east-1")
		# payload = {"message" : "invoked lambda"}
		# invoke_response = invokeLam.invoke(FunctionName = "AppstreamDemo", InvocationType = "Event", Payload = json.dumps(payload))
		# print(invoke_response)
	else:
	  print("Nothing requested")


def launch_stack():
  cfn = boto3.client('cloudformation')
  current_ts = datetime.now().isoformat().split('.')[0].replace(':','-')
  stackname = 'AppStream-Demo-' + current_ts
  capabilities = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']
  try:
    #template_params = parse_params()
    stackdata = cfn.create_stack(
      StackName=stackname,
      DisableRollback=True,
      TemplateURL=template_url,
      #Parameters=template_params,
      Capabilities=capabilities)
  except Exception as e:
    error_msg = str(e)
    print(error_msg)
    stackdata = {"error": error_msg}
  return stackdata  

def stack_success(stackdata):
  if 'error' in stackdata:
    return False
  else:
    return True

