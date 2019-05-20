from app import app
import yaml
from .libguides_request import Subject
from boto.s3.connection import S3Connection
import os

settings = yaml.safe_load(open('config.yml', 'r'))
api_key = S3Connection(os.environ['api-key'])


@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"


for subject in settings['subjects']:
    @app.route(f"/{str(subject)}", methods=['GET'])
    def route_subject():
        x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                    f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                    f"&key={api_key}", subject,
                    f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
        return x.create_document()
