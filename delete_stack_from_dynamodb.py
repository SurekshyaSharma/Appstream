


    #   Environment:
    #     Variables:
    #       stackName: !Ref 'StackName'
    #   Handler: "index.handler"
    #   Runtime: "python3.6"
    #   Timeout: "5"
    #   Role: !GetAtt DeleteCFNLambdaExecutionRole.Arn
    # ---------------------------------------------------------------------
    
def delete_stack(input):
     inputData = json.loads(input.formData)
    # {
    #   "Faculty Name":"vicky",
    #   "Department":"its",
    #   "StartTime":"2020-10-21T10:30",
    #   "EndTime":"2020-10-21T15:00",
    #   "Number of Instances":"1",
    #   "Index Code":"40810",
    #   "AppStream Package":"1",
    #   "invalidCheck":"",
    #   "":""
    # }
    for i in range(len(input)):
  	    stackname = 'AppStream-Demo-' + input.formId + i

  cfn = boto3.client('cloudformation')
  capabilities = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']
  try:
    #template_params = parse_params()
    stackdata = cfn.delete_stack(
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

    
def lambda_handler(event, context):

	#using now() to get current time 
	current_date = datetime.now(pytz.timezone('US/Central'))
	current_date_string = current_date.strftime("%Y-%m-%dT")

	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('serverlessrepo-serverless-form-handler-FormDataTable-1UNKJ1074YHCK')

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
        for i in range(len(items)):
            stack_result=delete_stack(items[i])
            print(stack_result)


        # ==================
	  if stack_success(stack_result):
	   resp_txt = "Your stack has been deleted. Please visit the AWS Console to confirm deletion"
	  else:
	   resp_txt = "Your stack failed to delete. Please visit the AWS Console to investigate further"

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
	  print("Nothing to delete")


      #Autodeletion 
          import boto3
          import os
          import json
          
          stack_name = os.environ['stackName']
          
          def delete_cfn(stack_name):
              try:
                  cfn = boto3.resource('cloudformation')
                  stack = cfn.Stack(stack_name)
                  stack.delete()
                  return "SUCCESS"
              except:
                  return "ERROR" 

          def handler(event, context):
              print("Received event:")
              print(json.dumps(event))
              return delete_cfn(stack_name)
          
