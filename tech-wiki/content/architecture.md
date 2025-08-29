---
title: "System Architecture"
draft: false
---

# System Architecture

## Overall Architecture

The COLD platform uses a multi-tier architecture:

1. **Data Layer**: 
   - PostgreSQL database for data storage and direct integration with NocoDB and web app

2. **Application Layer**:
   - API interface to PostgreSQL
   - Custom web application for public access
   - Container-based microservices for specific functionality

3. **Presentation Layer**:
   - Web interface accessible at https://cold.global
   - Administrative interface for research team (NocoDB)

## Database Architecture

The system uses a relational database model with multiple interconnected tables. The database structure is organized to represent relationships between different legal concepts and objects through linked record fields.

### Key Components

NocoDB --> PostgreSQL DB --> FastAPI Backend --> Public Facing Nuxt.js Frontend
