import requests


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
        return {
            'total_databases': self.total_databases,
            'featured_databases': self.databases,
            'associated_libguides': self.libguides
        }
