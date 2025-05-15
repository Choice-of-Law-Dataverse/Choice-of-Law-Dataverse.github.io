import json

class DataFilter:
    def __init__(self, input_file):
        self.input_file = input_file

    def load_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def filter_data(self, data):
        for table in data:
            table['fields'] = [field for field in table['fields'] if field['description'] != "No description"]
        return data

    def save_filtered_data(self, data, output_file):
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Filtered data saved to {output_file}")

# Example usage:
# filter = DataFilter('schema/airtable_metadata.json')
# data = filter.load_data()
# filtered_data = filter.filter_data(data)
# filter.save_filtered_data(filtered_data, 'schema/filtered_data.json')
