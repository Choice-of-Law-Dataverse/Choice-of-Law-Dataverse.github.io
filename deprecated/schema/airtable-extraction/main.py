from metadata_extractor import AirtableMetadataExtractor
from data_filter import DataFilter
from data_writer import DataWriter

def main():
    # Extract metadata
    extractor = AirtableMetadataExtractor(api_key=None, base_id='appz9Ei9mu9NIGmbK')
    initial_metadata = extractor.extract_metadata()
    extractor.save_metadata(initial_metadata, 'schema/airtable_info.json')

    # Filter metadata
    filter = DataFilter('schema/airtable_info.json')
    data = filter.load_data()
    filtered_data = filter.filter_data(data)
    filter.save_filtered_data(filtered_data, 'schema/airtable_info_filtered.json')

    # Write initial and filtered data to JSON, Markdown, and PDF
    data_writer = DataWriter(initial_metadata, filtered_data)
    data_writer.write_to_json(initial_metadata, 'schema/airtable_info.json')
    data_writer.write_to_markdown(initial_metadata, 'schema/airtable-extraction/airtable_info.md')
    data_writer.write_to_pdf(initial_metadata, 'schema/airtable-extraction/airtable_info.pdf')
    data_writer.write_to_json(filtered_data, 'schema/airtable_info_filtered.json')
    data_writer.write_to_markdown(filtered_data, 'schema/airtable-extraction/airtable_info_filtered.md')
    data_writer.write_to_pdf(filtered_data, 'schema/airtable-extraction/airtable_info_filtered.pdf')

if __name__ == "__main__":
    main()
