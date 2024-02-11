-- Databricks notebook source
CREATE SCHEMA IF NOT EXISTS control

-- COMMAND ----------

-- Creating the table for the metadata used by ADF pipelines
CREATE OR REPLACE TABLE Control.control_process(
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
COMMENT "table with metadata for ADF pipelines"

-- COMMAND ----------

-- Inserting metadata for ingesting orders to raw
INSERT INTO control.control_process VALUES(
  1,
  "orders_landingzone",
  "",
  "process that ingests orders data from source to landingzone",
  "orders",
  "Northwind.Orders",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/orders",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "order_details_landingzone",
  "",
  "process that ingests orders details data from source to landingzone",
  "order_details",
  "Northwind.OrderDetails",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/order_details",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "categories_landingzone",
  "",
  "process that ingests categories data from source to landingzone",
  "categories",
  "Northwind.Categories",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/categories",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "customers_landingzone",
  "",
  "process that ingests customers data from source to landingzone",
  "customers",
  "Northwind.Customers",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/customers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "products_landingzone",
  "",
  "process that ingests products data from source to landingzone",
  "products",
  "Northwind.Products",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/products",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "employees_landingzone",
  "",
  "process that ingests employees data from source to landingzone",
  "employees",
  "Northwind.Employees",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/employees",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "shippers_landingzone",
  "",
  "process that ingests shippers data from source to landingzone",
  "shippers",
  "Northwind.Shippers",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/shippers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  1,
  "suppliers_landingzone",
  "",
  "process that ingests suppliers data from source to landingzone",
  "suppliers",
  "Northwind.Suppliers",
  "",
  "",
  "landingzone",
  "adlsnorthwinddataprd",
  "northwind/suppliers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "suppliers_bronze",
  "/databricks_resources/1_bronze/dynamic_ladingzone_bronze",
  "process that ingests suppliers data from source to landingzone",
  "suppliers",
  "Northwind.Suppliers",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/suppliers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "shippers_bronze",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests shippers data from source to landingzone",
  "shippers",
  "Northwind.Shippers",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/shippers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "orders_bronze",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests shippers data from source to landingzone",
  "orders",
  "Northwind.Orders",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/orders",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "order_details_bronze",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests order_details data from source to landingzone",
  "order_details",
  "Northwind.OrderDetails",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/order_details",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "products_bronze",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests products data from source to landingzone",
  "products",
  "Northwind.Products",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/products",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "categories",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests categories data from source to landingzone",
  "categories",
  "Northwind.Categories",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/categories",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "customers",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests customers data from source to landingzone",
  "customers",
  "Northwind.Customers",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/customers",
  ""
)

-- COMMAND ----------

INSERT INTO control.control_process VALUES(
  2,
  "employees",
  "/databricks_resources/1_bronze/dynamic_landingzone_bronze",
  "process that ingests employees data from source to landingzone",
  "employees",
  "Northwind.E mployees",
  "",
  "",
  "bronze",
  "adlsnorthwinddataprd",
  "northwind/employees",
  ""
)
