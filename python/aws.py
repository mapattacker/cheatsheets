import boto3
import os
import json


access_key = ''
secret_key = ''



# S3 BUCKET ------------
bucket = "bucketname"
s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
my_bucket = s3.Bucket(bucket)

# download images from s3
# arg: (bucket-img-path, local-path)
bucket_raw_folder = 'public/raw_images/'
image = os.path.join(bucket_raw_folder, '1589792064372.jpeg')
my_bucket.download_file(image, 'test.jpeg')

# upload images to s3
# arg: (local-img-path, bucket-img-path)
local_img = '/Users/siyang/Desktop/siyang_test.jpg'
my_bucket.upload_file(local_img, 'public/label_images/siyang_test.jpg')

# list all files
for file in my_bucket.objects.all():
    print(file.key)



# DYNAMODB ------------
# with "id" as the primary key
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html
tableNm = 'table name in dynamodb'
dynamo = boto3.resource('dynamodb', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
table = dynamo.Table(tableNm)



# prints entire table
response = table.scan()
print(json.dumps(response, indent=2))



# query item by key
from boto3.dynamodb.conditions import Key, Attr
response = table.query(KeyConditionExpression=Key('id').eq('f486a80b-502d-4f69-8452-072847a188e1'))



# query by attributes, where clause
    # operators ---------------
    # eq = equal; lt = less than; gte = greater than
    # chains ------------------
    # & = and; | = or; ~ = not
from boto3.dynamodb.conditions import Key, Attr
response = table.scan(FilterExpression=Attr('view').eq("normal"))
print(response)



# update item by key
violations = {"food": "pass", "document": "pass", "security": "pass", "confidential": "fail"}
table.update_item(
    Key={'id': 'f486a80b-502d-4f69-8452-072847a188e1'},
    UpdateExpression='SET #attr = :val1',
    ExpressionAttributeNames={'#attr': 'violations'},
    ExpressionAttributeValues={':val1': None})


# insert new records to table
table.put_item(Item= {"label_img_url": "test_label_img_url",
                      "raw_img_url": "testing",
                      "label_text": "siyang_test",
                      "view": "normal",
                      "id": "12313",
                      "timestamp": "2020-05-19T08:27:18.139Z"})