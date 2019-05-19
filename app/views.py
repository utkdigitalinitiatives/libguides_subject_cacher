from app import app
import yaml
from .libguides_request import Subject

settings = yaml.safe_load(open('config.yml', 'r'))
subjects = settings['subjects']

for subject in subjects:
    @app.route(f"/{str(subject)}", methods=['GET'])
    def route_subject():
        x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                    f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                    f"&key={settings['api_key']}", subject,
                    f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={settings["api_key"]}&expand=owner')
        return x.create_document()
