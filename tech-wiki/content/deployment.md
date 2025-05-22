---
title: "Deployment Guide"
draft: false
---

# Deployment Guide

## Production Environment

The COLD platform is deployed using Microsoft Azure services:

- **Web Application**: Accessible at https://www.cold.global
- **Database**: PostgreSQL instance on Azure
- **Container Orchestration**: Azure Kubernetes Service
- **Application Hosting**: Azure Container Apps

## Deployment Process

While specific deployment processes are not detailed in the data management plan, the following general workflow can be inferred:

1. Data is maintained in Airtable
2. Selected data is synchronized to the PostgreSQL database
3. Web application containers are deployed to Azure
4. Updates to the web application are managed through Azure's deployment tools

## Backup Procedures

Regular backup procedures have been established:

1. **Weekly Exports**: CSV exports from Airtable 
2. **Storage**: Backups are stored on:
   - University of Lucerne network server
   - SwitchDrive
   - OneDrive
3. **Automation**: An automated process has been implemented for consistent backups

## Environment Management

### Production
- Live system accessible to the public at https://www.cold.global

### Development/Staging
- Not explicitly mentioned in the DMP, but implied through development workflow

## Access Management

- **Database Access**: Limited to research team members
- **Administrative Access**: Senior Researcher and Big Data assistant have admin rights
- **Public Access**: Read-only access to selected data through the web application

## Monitoring

- Airtable provides activity tracking and revision history for up to six months
- Record-level change tracking shows who made changes and what was modified
