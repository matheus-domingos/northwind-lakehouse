# Northwind Data Lakehouse

## Introduction
This project aims to extract Northwind data from a relational database (RDS AWS) and load it into a Datarbicks data lakehouse based on Microsoft Azure storage account.

## Extraction
The extraction is done by Azure Data Factory though a pipeline called source_landingzone.

## Bronze Layer
Data is being moved from a landingzone into a bronze layer using an dynamic Azure Datbricks notebook that receives table name from a ADF lookup, adds metadata and them save using structured streaming for batch and autoloader.

## Orchestration
The pipelines are orchestrated by Azure Data Factory. The process is metadata driven, where the name of the table, source and target are selected from a control table stored databricks catalog.

## Secrets
All sensitive information is managed by Azure Key Vault.
