
import boto3
import os
import json
 
def lambda_handler(event, context):
    print("Received event:")
    print(json.dumps(event))
 
    # stack_name = os.environ['stackName']
    stackNames = ["AppStream-SPSS-AO","AppStream-SPSS-OnDemand","AppStream-Other"]
    resp_txt = ''
 
    if len(stackNames) != 0:
        for i in range(len(stackNames)):
            stack_result = delete_cfn(stackNames[i])
            
            if stack_success(stack_result):
                # resp_txt = "Your stack has been deleted. Please visit the AWS Console to confirm deletion"
                resp_txt += stackNames[i] + ' has begun deletion. '
            else:
                resp_txt += stackNames[i] + ' was not deleted. '
                # resp_txt = "Your stack failed to delete. Please visit the AWS Console to investigate further"

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
        # invokeLam = boto3.client("lambda", region_name="us-east-1") payload = {"message" : "invoked lambda"} 
        # invoke_response = invokeLam.invoke(FunctionName = "AppstreamDemo", InvocationType = "Event", 
        # Payload = json.dumps(payload)) print(invoke_response) 
    else:
        json_resp = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Nothing to delete"
                },
                "shouldEndSession": "true"
            }
        }
        
        return json_resp

     
 
def delete_cfn(stackNames): #
    try:
        cfn = boto3.resource('cloudformation')
        stack = cfn.Stack(stackNames)

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.delete
        # Deletes a specified stack. Once the call completes successfully, stack deletion starts. 
        # Deleted stacks do not show up in the DescribeStacks API if the deletion has been completed successfully.
        stackDelte = stack.delete()
        return "SUCCESS"
    except:
        return "ERROR" 

def stack_success(stackdata):
  if stackdata == 'ERROR':
    return False
  else:
    return True
