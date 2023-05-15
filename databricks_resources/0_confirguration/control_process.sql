-- Databricks notebook source
-- Creating database for storing metadata to be used by ADF pipelines
CREATE DATABASE control
COMMENT "Datase used for pipelines"

-- COMMAND ----------

-- Creating the table for the metadata used by ADF pipelines
CREATE OR REPLACE TABLE control.control_process(
  process_level_id INT,
  process_name STRING,
  process_folder_path STRING,
  process_description STRING,
  process_source_name STRING,
  process_source_location STRING,
  process_source_container STRING,
  process_source_storage_account STRING,
  process_target_container STRING,
  process_target_storage_account STRING,
  process_target_location STRING,
  process_query_overwrite STRING
)
COMMENT "table with metadata for ADF pipeline"

-- COMMAND ----------

-- Inserting metadata for ingesting orders to raw
INSERT INTO control.control_process VALUES(
  1,
  "orders_raw",
  "",
  "process that ingests orders data from source to raw",
  "orders",
  "Northwind.Orders",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "orders",
  ""
)
