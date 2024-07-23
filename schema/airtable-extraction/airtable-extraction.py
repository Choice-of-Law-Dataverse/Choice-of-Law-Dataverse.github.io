import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with your Airtable API key and Base ID
API_KEY = os.getenv('AIRTABLE_API_KEY')
BASE_ID = 'appz9Ei9mu9NIGmbK'
ENDPOINT = f'https://api.airtable.com/v0/meta/bases/{BASE_ID}/tables'

# Set up headers with the API key for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

# Make the request to the Metadata API
response = requests.get(ENDPOINT, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    metadata = response.json()
    metadata_dict = []

    # Iterate over the tables and print their descriptions
    for table in metadata['tables']:
        table_info = {
            'table': table['name'],
            'description': table.get('description', 'No description'),
            'fields': []
        }
        # Iterate over the fields in the table and print their descriptions
        for field in table['fields']:
            field_info = {
                'field': field['name'],
                'description': field.get('description', 'No description'),
                'type': field['type']
            }
            table_info['fields'].append(field_info)
    
        metadata_dict.append(table_info)
    
    with open('schema/airtable_metadata.json', 'w') as f:
        json.dump(metadata_dict, f, indent=4)
    print(f"Metadata saved to airtable_metadata.json")
else:
    print(f"Failed to retrieve metadata: {response.status_code} - {response.text}")
