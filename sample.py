# download------------S3file--------------------------------------
import boto3
bucketname = 'my-bucket' # replace with your bucket name
filename = 'my_image_in_s3.jpg' # replace with your object key
s3 = boto3.resource('s3')
s3.Bucket(bucketname).download_file(filename, 'my_localimage.jpg')
# download------------S3file--------------------------------------

# Open the text file------------S3file--------------------------------------
s3 = boto3.resource('s3')
bucket = s3.Bucket('test-bucket')
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
# Open the text file------------S3file--------------------------------------
