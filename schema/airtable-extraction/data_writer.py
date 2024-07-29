import json
import markdown2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

class DataWriter:
    def __init__(self, data, filtered_data):
        self.data = data
        self.filtered_data = filtered_data

    def write_to_json(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")

    def write_to_markdown(self, data, filename):
        markdown_content = "# Data\n\n"
        for table in data:
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

    def write_to_pdf(self, data, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleH = styles['Heading1']

        elements.append(Paragraph("Data", styleH))

        for table in data:
            elements.append(Paragraph(f"Table: {table['table']}", styleH))
            elements.append(Paragraph(f"Description: {table['description']}", styleN))

            table_data = [["Field", "Description", "Type"]]
            for field in table['fields']:
                table_data.append([field['field'], field['description'], field['type']])

            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            table_element = Table(table_data)
            table_element.setStyle(table_style)

            elements.append(table_element)
            elements.append(Paragraph(" ", styleN))  # Add space between tables

        doc.build(elements)
        print(f"Data saved to {filename}")

# Example usage:
# data_writer = DataWriter(initial_data, filtered_data)
# data_writer.write_to_json(initial_data, 'schema/airtable-extraction/initial_data.json')
# data_writer.write_to_markdown(initial_data, 'schema/airtable-extraction/initial_data.md')
# data_writer.write_to_pdf(initial_data, 'schema/airtable-extraction/initial_data.pdf')
# data_writer.write_to_json(filtered_data, 'schema/airtable-extraction/filtered_data.json')
# data_writer.write_to_markdown(filtered_data, 'schema/airtable-extraction/filtered_data.md')
# data_writer.write_to_pdf(filtered_data, 'schema/airtable-extraction/filtered_data.pdf')
