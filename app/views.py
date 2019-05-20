from app import app
import yaml
from .libguides_request import Subject
import os
import sys
from flask import jsonify


print("Starting Flask")
sys.stdout.flush()

settings = yaml.safe_load(open('config.yml', 'r'))
api_key = os.environ['api-key']

print("Creating Routes")
sys.stdout.flush()


# @app.route('/', methods=['GET'])
# def index():
#     return "Hello, World!"
#
#
# for subject in settings['subjects']:
#     @app.route(f"/{str(subject)}", methods=['GET'])
#     def route_subject():
#         print(f"Attempting to create route for {subject}.")
#         x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
#                     f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
#                     f"&key={api_key}", subject,
#                     f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
#         sys.stdout.flush()
#         return jsonify(x.create_document())


@app.route('/<page>', methods=['GET'])
def route_subject(page):
    print(f"Attempting to create route for {page}")
    x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                f"&key={api_key}", page,
                f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
    sys.stdout.flush()
    return jsonify(x.create_document())


# @app.route('/39797', methods=['GET'])
# def route_biology():
#     print(f"Attempting to create route for 39797.")
#     x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
#                         f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
#                         f"&key={api_key}", 39797,
#                         f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={api_key}&expand=owner')
#     sys.stdout.flush()
#     return jsonify(x.create_document())
