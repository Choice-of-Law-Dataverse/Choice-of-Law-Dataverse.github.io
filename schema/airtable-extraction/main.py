from metadata_extractor import AirtableMetadataExtractor
from data_filter import DataFilter
from data_writer import DataWriter

def main():
    # Extract metadata
    extractor = AirtableMetadataExtractor(api_key=None, base_id='appz9Ei9mu9NIGmbK')
    metadata = extractor.extract_metadata()
    extractor.save_metadata(metadata, 'schema/airtable_metadata.json')

    # Filter metadata
    filter = DataFilter('schema/airtable_metadata.json')
    data = filter.load_data()
    filtered_data = filter.filter_data(data)
    filter.save_filtered_data(filtered_data, 'schema/filtered_data.json')

    # Write filtered data to JSON, Markdown, and PDF
    data_writer = DataWriter(filtered_data)
    data_writer.write_to_json('schema/filtered_data.json')
    data_writer.write_to_markdown('schema/filtered_data.md')
    data_writer.write_to_pdf('schema/filtered_data.pdf')

if __name__ == "__main__":
    main()
