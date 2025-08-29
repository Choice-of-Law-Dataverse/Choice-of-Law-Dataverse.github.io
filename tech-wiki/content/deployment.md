---
title: "Deployment Guide"
draft: false
---

# Deployment Guide

## Production Environment

The COLD platform is deployed using Microsoft Azure services:

- **Web Application**: Accessible at https://www.cold.global
- **Database**: PostgreSQL instance on Azure
- **Application Hosting**: Azure Container Apps

## Deployment Process

1. Data is maintained in NocoDB
2. Data is permanently synchronized to the PostgreSQL database
3. Web application containers are deployed to Azure
4. Updates to the web application are managed through Azure's deployment tools

## Backup Procedures

Regular backup procedures have been established through the built-in backup tools within the Azure flexible server for PostgreSQL

## Environment Management

### Production
- Live system accessible to the public at https://www.cold.global

### Development/Staging
- only one website version is live. The state of code on the gitub repository's branch "prod" is automatically connected to the deployment via CI/CD

## Access Management

- **Database Access**: Limited to research team members
- **Administrative Access**: Senior Researcher and Big Data assistant have admin rights
- **Public Access**: Read-only access to selected data through the web application

## Monitoring

- NocoDB provides activity tracking and revision history for up to six months
- Record-level change tracking shows who made changes and what was modified
