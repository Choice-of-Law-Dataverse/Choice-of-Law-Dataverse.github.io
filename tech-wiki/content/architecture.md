---
title: "System Architecture"
draft: false
---

# System Architecture

## Overall Architecture

The COLD platform uses a multi-tier architecture:

1. **Data Layer**: 
   - Primary data storage in Airtable cloud database
   - PostgreSQL database for the public-facing web application

2. **Application Layer**:
   - API interface to Airtable for data management
   - Custom web application for public access
   - Container-based microservices for specific functionality

3. **Presentation Layer**:
   - Web interface accessible at cold.global
   - Administrative interface for research team

## Database Architecture

The system uses a relational database model with multiple interconnected tables. The database structure is organized to represent relationships between different legal concepts and objects through linked record fields.

### Key Components

Airtable Base --> PostgreSQL DB --> FastAPI Backend --> Public Facing Nuxt.js Frontend

## Backup System

- Regular exports from Airtable to CSV format
- Storage of backups on SwitchDrive and OneDrive
- Automated backup procedures for data consistency
- Retention of historical data for at least five years
