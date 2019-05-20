from apscheduler.schedulers.blocking import BlockingScheduler
import yaml
from libguides_request import Subject
import os
import sys

schedule = BlockingScheduler()


@schedule.scheduled_job('cron', day_of_week='mon-sun', hour=18, minute=38)
def scheduled_job():
    print("Running Scheduled Job")
    settings = yaml.load(open('../config.yml'), 'r')
    api_key = os.environ.get(['api-key'])
    for subject in settings['subjects']:
        print(f'Generating JSON for {subject}')
        with open(f'templates/{subject}', 'w') as my_json:
            x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                        f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                        f"&key={api_key}", subject,
                        f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
            my_json.write(x.create_document())
        sys.stdout.flush()
    return


schedule.start()
