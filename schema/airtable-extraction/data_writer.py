import json
import markdown2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

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
        styleP = ParagraphStyle(name='Normal', fontSize=10)

        elements.append(Paragraph("Data", styleH))
        elements.append(Spacer(1, 12))

        for table in data:
            elements.append(Paragraph(f"Table: {table['table']}", styleH))
            elements.append(Paragraph(f"Description: {table['description']}", styleN))
            elements.append(Spacer(1, 12))

            table_data = [["Field", "Description", "Type"]]
            for field in table['fields']:
                table_data.append([
                    Paragraph(field['field'], styleP),
                    Paragraph(field['description'], styleP),
                    Paragraph(field['type'], styleP)
                ])

            table_element = Table(table_data)
            table_element.setStyle(self._get_table_style())

            # Adjust column widths to fit within the page
            col_widths = self._get_column_widths(table_data, doc.width)
            table_element._argW = col_widths

            elements.append(table_element)
            elements.append(Spacer(1, 24))

        doc.build(elements)
        print(f"Data saved to {filename}")

    def _get_table_style(self):
        return TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

    def _get_column_widths(self, table_data, max_width):
        # Calculate the maximum width for each column
        num_cols = len(table_data[0])
        col_widths = [max_width / num_cols] * num_cols

        for row in table_data:
            for i, cell in enumerate(row):
                if isinstance(cell, Paragraph):
                    cell_width = self._get_text_width(cell.getPlainText())
                else:
                    cell_width = self._get_text_width(str(cell))
                if cell_width > col_widths[i]:
                    col_widths[i] = cell_width

        # Ensure the total width does not exceed the max_width
        total_width = sum(col_widths)
        if total_width > max_width:
            scale_factor = max_width / total_width
            col_widths = [width * scale_factor for width in col_widths]

        return col_widths

    def _get_text_width(self, text, font_size=10, font_name="Helvetica"):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        return stringWidth(text, font_name, font_size)

# Example usage:
# data_writer = DataWriter(initial_data, filtered_data)
# data_writer.write_to_json(initial_data, 'schema/airtable-extraction/initial_data.json')
# data_writer.write_to_markdown(initial_data, 'schema/airtable-extraction/initial_data.md')
# data_writer.write_to_pdf(initial_data, 'schema/airtable-extraction/initial_data.pdf')
# data_writer.write_to_json(filtered_data, 'schema/airtable-extraction/filtered_data.json')
# data_writer.write_to_markdown(filtered_data, 'schema/airtable-extraction/filtered_data.md')
# data_writer.write_to_pdf(filtered_data, 'schema/airtable-extraction/filtered_data.pdf')
