import os
import boto3, botocore
import json
import datetime
import re
from flask import Flask, request, redirect
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

@app.route("/")
def hello():
    return "<h1>Hello!</h1>"

"""
Receives data from `kubectl preflight` command and redirects it to an S3 bucket.
"""
@app.route("/preflight", methods=['POST'])
def preflight():
    try:
        s3_key = 'Preflight' + str(datetime.datetime.now().timestamp()) + ".json"
        return upload_to_s3(json.dumps(request.json), os.getenv('AWS_BUCKET_NAME'), s3_key)

    except Exception as e:
        print("Error: ", e)
        return e

"""
Receives data from `kubectl support-bundle` command and redirects it to an S3 bucket.
"""
@app.route("/bundle", methods=['POST'])
def bundle():
    try:
        s3_key = 'support-bundle' + str(datetime.datetime.now().timestamp()) + ".tar.gz"
        return upload_to_s3(request.data, os.getenv('AWS_BUCKET_NAME'), s3_key)

    except Exception as e:
        print("Error: ", e)
        return e


def upload_to_s3(body, bucket, key):
    result = s3.put_object(
        Body=body,
        Bucket=bucket,
        Key=key
    )
    
    if result['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = os.getenv('AWS_DOMAIN') + key
    else:
        response = False

    print(response)    
    return response

if __name__ == '__main__':
    app.run()

