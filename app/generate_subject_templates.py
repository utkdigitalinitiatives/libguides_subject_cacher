from apscheduler.schedulers.blocking import BlockingScheduler
from libguides_request import Subject
import os
import sys
import boto3
import json

schedule = BlockingScheduler()
api_key = os.environ['api-key']
subjects = os.environ['subjects'].split(',')
bucket = os.environ['S3_bucket_name']
secret_key = os.environ['S3_secret_key']
access_key = os.environ['S3_access_key']
hour = int(os.environ['hour'])
minute = int(os.environ['minute'])
s3_connection = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key
                             )


@schedule.scheduled_job('cron', day_of_week='mon-sun', hour=hour, minute=minute)
def scheduled_job():
    print("Running Scheduled Job")
    for subject in subjects:
        print(f'Generating JSON for {subject}')
        x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                    f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                    f"&key={api_key}", subject,
                    f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
        json_response = json.dumps(x.create_document())
        json_string = json.loads(json_response)
        print(json_string)
        sys.stdout.flush()
        s3_connection.put_object(Body=str.encode(json_string), Bucket=bucket, Key=f'responses/{subject}')
    return


schedule.start()
