import json

# Function to read JSON data from a file
def load_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to filter out fields with "No description"
def filter_fields(data):
    filtered_data = []
    for table in data:
        filtered_fields = [field for field in table['fields'] if field['description'] != 'No description']
        if filtered_fields:
            filtered_data.append({
                "table": table["table"],
                "fields": filtered_fields
            })
    return filtered_data

# Function to generate Mermaid diagram syntax with description and field type
def generate_mermaid(data):
    mermaid_syntax = 'graph TD\n'
    
    for table in data:
        table_name = table['table']
        for field in table['fields']:
            field_name = field['field']
            field_description = field['description']
            field_type = field['type']
            # Combine field name, description, and type in the label
            label = f"{field_name}\n{field_description}\n({field_type})"
            # Use HTML-like syntax for multi-line labels in Mermaid
            mermaid_syntax += f'    {table_name} --> |"{label}"| {field_name}\n'
    
    return mermaid_syntax

# Load JSON data from file
filename = 'schema/airtable_metadata.json'
json_data = load_json_from_file(filename)

# Apply filtering
filtered_data = filter_fields(json_data)

# Generate Mermaid syntax
mermaid_diagram = generate_mermaid(filtered_data)

# Print or save the Mermaid diagram syntax
print(mermaid_diagram)

# Optionally, save the Mermaid diagram syntax to a file
with open('schema/mermaid/mermaid_diagram.mmd', 'w') as file:
    file.write(mermaid_diagram)
