import json
import re

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

# Function to escape special characters for Mermaid
def escape_mermaid_string(text):
    if text is None:
        return ''
    # Escape quotes and backslashes
    text = text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    return text

# Function to convert to Pascal Case
def to_pascal_case(text):
    return ''.join(word.capitalize() for word in text.split())

# Function to remove quotation marks from a string
def remove_quotation_marks(text):
    return text.replace('"', '')

# Function to handle special characters and Pascal Case conversion
def process_field_name(name):
    name = escape_mermaid_string(name)
    # Replace spaces and special characters with underscores
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    return to_pascal_case(name)

# Function to generate Mermaid diagram syntax with description and field type
def generate_mermaid(data):
    mermaid_syntax = 'erDiagram\n'
    tables = {}

    for table in data:
        table_name = process_field_name(table['table'])
        if table_name not in tables:
            tables[table_name] = []

        for field in table['fields']:
            field_name = process_field_name(field['field'])
            field_description = remove_quotation_marks(escape_mermaid_string(field['description']))
            field_type = escape_mermaid_string(field['type'])

            # Combine field name, description, and type in the label
            label = f"{field_name}\\n{field_description}\\n({field_type})"
            tables[table_name].append(f'{field_name} {field_type} "{field_description}"')

    for table_name, fields in tables.items():
        mermaid_syntax += f'    {table_name} {{\n'
        mermaid_syntax += '\n'.join(f'        {field}' for field in fields)
        mermaid_syntax += '\n    }\n'

    return mermaid_syntax.strip()

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
