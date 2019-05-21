from apscheduler.schedulers.blocking import BlockingScheduler
from libguides_request import Subject
import os
import sys
import boto3
from boto3 import s3

schedule = BlockingScheduler()
api_key = os.environ['api-key']
subjects = os.environ['subjects'].split(',')
bucket = os.environ['S3_bucket_name']
secret_key = os.environ['S3_secret_key']
access_key = os.environ['S3_access_key']
s3_connection = boto3.resource('s3')


@schedule.scheduled_job('cron', day_of_week='mon-sun', hour=19, minute=47)
def scheduled_job():
    print("Running Scheduled Job")
    for subject in subjects:
        print(f'Generating JSON for {subject}')
        x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                    f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                    f"&key={api_key}", subject,
                    f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
        object = s3.Object(bucket, subject)
        object.put(Body=str.encode(x.create_document()))
        sys.stdout.flush()
    return


schedule.start()
