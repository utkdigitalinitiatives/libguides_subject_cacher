from app import app
import os
from flask import jsonify
import json
import boto3

api_key = os.environ['api-key']
bucket = os.environ['S3_bucket_name']
secret_key = os.environ['S3_secret_key']
access_key = os.environ['S3_access_key']
subjects = os.environ['subjects']
s3_connection = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key
                             )
responses_from_aws = {}

for subject in subjects:
    s3_object = s3_connection.get_object(Bucket=bucket, Key=f'responses/{subject}')
    body = s3_object['Body'].read()
    decoded = body.decode('utf-8')
    json_string = json.loads(decoded)
    responses_from_aws.update({subject: json_string})


@app.route('/<page>', methods=['GET'])
def route_subject(page):
    return jsonify(responses_from_aws[page])
