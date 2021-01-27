import boto3
import os
import json


access_key = os.environ["AWS_ACCESS_KEY_ID"]
secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]



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

# delete objects
from boto.s3.connection import S3Connection, Bucket, Key

conn = S3Connection(AWS_ACCESS_KEY, AWS_SECERET_KEY)
b = Bucket(conn, S3_BUCKET_NAME)
k = Key(b)
k.key = 'images/my-images/'+filename

b.delete_key(k)



def download_s3(s3folder, bucket="vama-sceneuds-images"):
    """download all data in a S3 folder"""
    s3 = boto3.client('s3')
    for obj in s3.list_objects_v2(Bucket=bucket, Prefix=s3folder)["Contents"]:
        s3_file = obj["Key"]
        s3_subfolder = s3_file.split("/")[-2]
        s3_filename = s3_file.split("/")[-1]
        local_subfolder_path = os.path.join("download", s3_subfolder)
        local_subfolder_filepth = os.path.join(local_subfolder_path, s3_filename)

        if not os.path.exists(local_subfolder_path):
            os.makedirs(local_subfolder_path)
        s3.download_file(bucket, s3_file, local_subfolder_filepth)

        print(s3_filename, "downloaded")



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