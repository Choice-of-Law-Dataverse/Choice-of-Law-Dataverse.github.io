import json
import markdown2
import pdfkit

class DataWriter:
    def __init__(self, data):
        self.data = data

    def write_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        print(f"Data saved to {filename}")

    def write_to_markdown(self, filename):
        markdown_content = "# Filtered Data\n\n"
        for table in self.data:
            markdown_content += f"## Table: {table['table']}\n\n"
            markdown_content += f"**Description**: {table['description']}\n\n"
            markdown_content += "| Field | Description | Type |\n"
            markdown_content += "|-------|-------------|------|\n"
            for field in table['fields']:
                markdown_content += f"| {field['field']} | {field['description']} | {field['type']} |\n"
            markdown_content += "\n"

        with open(filename, 'w') as file:
            file.write(markdown_content)
        print(f"Data saved to {filename}")

    def write_to_pdf(self, filename):
        # Convert markdown to HTML
        markdown_content = "# Filtered Data\n\n"
        for table in self.data:
            markdown_content += f"## Table: {table['table']}\n\n"
            markdown_content += f"**Description**: {table['description']}\n\n"
            markdown_content += "| Field | Description | Type |\n"
            markdown_content += "|-------|-------------|------|\n"
            for field in table['fields']:
                markdown_content += f"| {field['field']} | {field['description']} | {field['type']} |\n"
            markdown_content += "\n"

        html_content = markdown2.markdown(markdown_content)

        # Convert HTML to PDF
        pdfkit.from_string(html_content, filename)
        print(f"Data saved to {filename}")

# Example usage:
# data_writer = DataWriter(filtered_data)
# data_writer.write_to_json('schema/filtered_data.json')
# data_writer.write_to_markdown('schema/filtered_data.md')
# data_writer.write_to_pdf('schema/filtered_data.pdf')
