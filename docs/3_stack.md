# Technology Stack

## Database Technologies

### Primary Data Storage
- **Airtable**
  - Plus Plan subscription
  - Capacity for ~15,000 records per base
  - 5GB attachment storage per base
  - Relational database structure
  - Cloud-synced with Amazon Web Services infrastructure

### Secondary Database
- **PostgreSQL** on Azure
  - Stores data for public web interface
  - Synchronized with selected Airtable data

## Cloud Infrastructure

- **Microsoft Azure**
  - **Azure Container Apps**: Hosts containerized application components
  - **Azure Kubernetes Service**: Orchestrates containers for scalability
  - **Azure PostgreSQL**: Managed database service

## Development Tools

- **Airtable API**: For programmatic access to database content
- **Airtable Scripting Extension**: For metadata collection and automation

## Backup Tools

- **SwitchDrive**: University-provided cloud storage
- **OneDrive**: Secondary backup location
- **CSV Export**: Data format for backups

## Security & Compliance

- Airtable Security Features:
  - ISO/IEC 27001:2013 certification
  - SOC 2 compliance
  - GDPR compliance
  
## Web Application

- **Public-facing website**: https://www.cold.global
- **Content Delivery**: Details not specified in DMP
- **Authentication**: Role-based access for administration