---
title: "Data Structure and Management"
draft: false
---

# Data Structure and Management

## Database Structure

The database is organized into multiple related tables that store different types of legal information:

### Main Data Tables

1. **Answers** (14,942 records)
2. **HCCH Answers** (20 records)
3. **Domestic Instruments** (195 records)
4. **Domestic Legal Provisions** (99 records)
5. **Regional Instruments** (6 records)
6. **Regional Legal Provisions** (129 records)
7. **International Instruments** (1 record)
8. **International Legal Provisions** (22 records)
9. **Court Decisions** (1,321 records)
10. **Arbitral Institutions** (28 records)
11. **Arbitral Rules** (28 records)
12. **Arbitral Awards** (67 records)
13. **Literature** (217 records)

### Metadata Tables

1. **Themes** (15 records)
2. **Questions** (61 records)
3. **Jurisdictions** (249 records)
4. **Topics** (0 records)
5. **Glossary** (29 records)
6. **Abbreviations** (60 records)
7. **Specialists** (68 records)

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

In addition to structured data in Airtable:
- Original PDF files are stored in folders organized by region > country/region with an ID number
- File naming convention: YEAR_COURT_CHAMBER OR CIRCUIT_NAME OF THE CASE, e.g., "1976_United States Court of Appeals_Fifth Circuit_Baruch Foster Corporation v Imperial Ethiopian Government"

## Version Control

- Airtable provides record-level revision history for six months
- Shows who made changes and what was modified
- Comments remain in the activity feed until manually deleted

## Data Volume

- Structured data: Less than 100MB
- PDF attachments: Additional 5-10GB
