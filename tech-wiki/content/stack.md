---
title: "Technology Stack"
draft: false
---

# Technology Stack

## Database Technologies

### Primary Data Storage
- **PostgreSQL**
  - Runs on Azure
  - Stores data for both data management tool and the public web interface

### Data Management Tool
- **NocoDB** self hosted as a Container App on Azure
  - connected to PostgreSQL
  - Stores data and allows users to make edits
  - Synchronized with the web app

## Cloud Infrastructure

- **Microsoft Azure**
  - **Azure Container Apps**: Hosts containerized application components
  - **Azure PostgreSQL**: Managed database service

## Web Application

- **Public-facing website**: https://www.cold.global
