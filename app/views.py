from app import app
import yaml
from .libguides_request import Subject
import os
from flask import jsonify

settings = yaml.safe_load(open('config.yml', 'r'))
api_key = os.environ['api-key']


@app.route('/<page>', methods=['GET'])
def route_subject(page):
    x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                f"&key={api_key}", page,
                f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
    return jsonify(x.create_document())
