# rading the file in S3

import boto3
 
s3client = boto3.client(
    's3',
    region_name='us-east-1'
)
 
# These define the bucket and object to read
bucketname = mybucket 
file_to_read = /dir1/filename 

#Create a file object using the bucket and object key. 
fileobj = s3client.get_object(
    Bucket=bucketname,
    Key=file_to_read
    ) 
# open the file object and read it into the variable filedata. 
filedata = fileobj['Body'].read()

# file data will be a binary stream.  We have to decode it 
contents = filedata.decode('utf-8')) 

# Once decoded, you can treat the file as plain text if appropriate 
print(contents)


# uploading a file directly to S3    https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3
s3.Bucket('bucketname').upload_file('/local/file/here.txt','folder/sub/path/to/s3key')


# reading the read json from s3

import json, boto3
s3 = boto3.resource("s3").Bucket("bucket")
json.load_s3 = lambda f: json.load(s3.Object(key=f).get()["Body"])
json.dump_s3 = lambda obj, f: s3.Object(key=f).put(Body=json.dumps(obj))
# Now you can use json.load_s3 and json.dump_s3 with the same API as load and dump
data = {"test":0}
json.dump_s3(data, "key") # saves json to s3://bucket/key
data = json.load_s3("key") # read json from s3://bucket/key
#-----------------------------------------------------------------------------------------------------
# storing a list in S3 bucket   https://dzone.com/articles/boto3-amazon-s3-as-python-object-store
import boto3
import pickle
s3 = boto3.client('s3')
myList=[1,2,3,4,5]
#Serialize the object 
serializedListObject = pickle.dumps(myList)
#Write to Bucket named 'mytestbucket' and 
#Store the list using key myList001
s3.put_object(Bucket='mytestbucket',Key='myList001',Body=serializedListObject)

# retrieving a list from S3 Bucket

import boto3
import pickle
#Connect to S3
s3 = boto3.client('s3')
#Read the object stored in key 'myList001'
object = s3.get_object(Bucket='mytestbucket',Key='myList001')
serializedObject = object['Body'].read()
#Deserialize the retrieved object
myList = pickle.loads(serializedObject)
print myList

# storing the python Dictionary Object in S3

import boto3
import pickle
#Connect to S3 default profile
s3 = boto3.client('s3')
myData = {'firstName':'Saravanan','lastName':'Subramanian','title':'Manager', 'empId':'007'}
#Serialize the object
serializedMyData = pickle.dumps(myData)
#Write to S3 using unique key - EmpId007
s3.put_object(Bucket='mytestbucket',Key='EmpId007')

# Retrieving Python Dictionary Object From S3 Bucket

import boto3
s3 = boto3.client('s3')
object = s3.get_object(Bucket='mytestbucket',Key='EmpId007')
serializedObject = object['Body'].read()
myData = pickle.loads(serializedObject)
print myData

# Storing a Python Dictionary Object As JSON in S3 Bucket

import boto3
import json
s3 = boto3.client('s3')
myData = {'firstName':'Saravanan','lastName':'Subramanian','title':'Manager', 'empId':'007'}
serializedMyData = json.dumps(myData)
s3.put_object(Bucket='mytestbucket',Key='EmpId007')

# Retrieving a JSON From S3 Bucket

import boto3
import json
s3 = boto3.client('s3')
object = s3.get_object(Bucket='mytestbucket',Key='EmpId007')
serializedObject = object['Body'].read()
myData = json.loads(serializedObject)
print myData

# Uploading a File
import boto3
s3 = boto3.client('s3')
s3.upload_file(Bucket='mytestbucket', Key='subdir/abc.txt', Filename='./abc.txt')

# Download a File From S3 Bucket
import boto3
s3 = boto3.clinet('s3')
s3.download_file(Bucket='mytestbucket',Key='subdir/abc.txt',Filename='./abc.txt')

# Error Handling
import boto3
try:
s3 = s3.client('s3')
except Exceptions as e:
        print "Exception ",e
