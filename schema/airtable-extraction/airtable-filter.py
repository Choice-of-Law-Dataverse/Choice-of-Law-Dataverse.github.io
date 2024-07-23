import json

# Load your JSON data
with open('schema/airtable_metadata.json', 'r') as file:
    data = json.load(file)

# Function to filter out fields with "No description"
def filter_data(data):
    for table in data:
        table['fields'] = [field for field in table['fields'] if field['description'] != "No description"]
    return data

filtered_data = filter_data(data)

# Save the filtered data to a new file
with open('schema/filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
