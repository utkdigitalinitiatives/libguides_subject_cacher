import requests
import yaml
import json


class Subject:
    def __init__(self, database_request, subject_id, libguides_request):
        self.subject_id = str(subject_id)
        self.total_databases = 0
        self.database_request = f"{database_request}&subject_ids={subject_id}"
        self.libguides_request = f"{libguides_request}&subject_ids={subject_id}"
        self.databases = self.process_databases()
        self.libguides = self.process_libguides()

    def process_databases(self):
        response = requests.get(self.database_request).json()
        databases = []
        self.total_databases = len(response)
        for database in response:
            for resource in database['subjects']:
                if resource['featured'] == "1" and resource['id'] == self.subject_id:
                    databases.append(database)
        return databases

    def process_libguides(self):
        return requests.get(self.libguides_request).json()

    def create_document(self):
        return json.dumps({
            'total_databases': self.total_databases,
            'featured_databases': self.databases,
            'associated_libguides': self.libguides
        })


if __name__ == "__main__":
    settings = yaml.safe_load(open('config.yml', 'r'))
    for subject in settings['subjects']:
        with open(f'app/templates/{subject}', 'w') as my_json:
            x = Subject(f"https://lgapi-us.libapps.com/1.1/assets?site_id=681&asset_types=10&expand="
                        f"permitted_uses,az_types,az_props,subjects,icons,friendly_url,permitted_uses"
                        f"&key={settings['api_key']}", subject,
                        f'http://lgapi-us.libapps.com/1.1/guides?site_id=681&key={settings["api_key"]}&expand=owner')
            my_json.write(x.create_document())
