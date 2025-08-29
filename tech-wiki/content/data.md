---
title: "Data Structure and Management"
draft: false
---

# Data Structure and Management

## Database Structure

The database is organized into multiple related tables that store different types of legal information:

### Main Data Tables

1. **Answers**
2. **HCCH Answers**
3. **Domestic Instruments**
4. **Domestic Legal Provisions**
5. **Regional Instruments**
6. **Regional Legal Provisions**
7. **International Instruments**
8. **International Legal Provisions**
9. **Court Decisions**
10. **Arbitral Institutions**
11. **Arbitral Rules**
12. **Arbitral Awards**
13. **Literature**

### Metadata Tables

1. **Themes**
2. **Questions**
3. **Jurisdictions**
4. **Topics**
5. **Glossary**
6. **Abbreviations**
7. **Specialists**

## Airtable Configuration

### Components
- **Base**: Collection of all data tables
- **Table**: Individual data tables within the base
- **Field**: Columns within tables (various data types)
- **Record**: Individual rows within tables
- **Views**: Saved configurations of filtered, sorted, or grouped data

### Naming Conventions
- Table and Field names follow title case capitalization per APA guidelines
- "Linked" columns are named `<TABLE NAME> "Link"`
- Lookup columns are named `<TABLE NAME> <COLUMN NAME>`

## Data Entry Rules

### For Answers/Questions/Jurisdictions Tables
1. Use search/filter/group functions to locate records
2. Edit existing fields as needed
3. Do not add new entries to these tables
4. For answers, select from predefined dropdown options

### For Legal Provisions/Court Decisions/Arbitral Awards Tables
1. Add new records as needed
2. Edit existing information directly in the relevant fields

### For Concepts
- Edit existing fields
- Use "Assignee" column to define responsibilities

## File Storage

In addition to structured data in NocoDB:
- Original PDF files are stored in an Azure storage account named with their respective CoLD ID
- File naming convention: follows the CoLD ID logic, i.e. "CD-CHE-1020"

## Data Volume

- Structured data: Less than 100MB
- PDF attachments: Additional 5-10GB
