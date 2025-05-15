import requests
import json
import os
from dotenv import load_dotenv

class AirtableMetadataExtractor:
    def __init__(self, api_key, base_id):
        load_dotenv()
        self.api_key = api_key or os.getenv('AIRTABLE_API_KEY')
        self.base_id = base_id
        self.endpoint = f'https://api.airtable.com/v0/meta/bases/{self.base_id}/tables'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
        }

    def fetch_metadata(self):
        response = requests.get(self.endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve metadata: {response.status_code} - {response.text}")

    def extract_metadata(self):
        metadata = self.fetch_metadata()
        metadata_dict = []

        for table in metadata['tables']:
            table_info = {
                'table': table['name'],
                'description': table.get('description', 'No description'),
                'fields': []
            }
            for field in table['fields']:
                field_info = {
                    'field': field['name'],
                    'description': field.get('description', 'No description'),
                    'type': field['type']
                }
                table_info['fields'].append(field_info)
        
            metadata_dict.append(table_info)
        
        return metadata_dict

    def save_metadata(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Metadata saved to {filename}")

# Example usage:
# extractor = AirtableMetadataExtractor(api_key='your_api_key', base_id='your_base_id')
# metadata = extractor.extract_metadata()
# extractor.save_metadata(metadata, 'schema/airtable_metadata.json')
