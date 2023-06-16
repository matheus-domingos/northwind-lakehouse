# Databricks notebook source
# MAGIC %run ../0_configuration/connect_adls

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.orders(OrderID int, CustomerID int, EmployeeID int, OrderDate TIMESTAMP, ShipperID int, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/orders'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE TABLE bronze_northwind.order_details(OrderDetailID int, OrderID int, ProductID int, Quantity int, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/order_details'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.categories(CategoryID int, CategoryName STRING, Description STRING, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/categories'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.customers(CustomerID int, CustomerName STRING, ContactName STRING, Address STRING, City STRING, PostalCode STRING, Country STRING, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/customers'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.employees(EmployeeID int, LastName STRING, FirstName STRING, BirthDate TIMESTAMP, Photo STRING, Notes STRING, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/employees'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.products(ProductID int, ProductName STRING, SupplierID int, CategoryID int, Unit STRING, Price DOUBLE, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/products'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE table bronze_northwind.shippers(ShipperID int, ShipperName STRING, Phone STRING,_metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP, source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/shippers'" )

# COMMAND ----------

spark.sql(f"CREATE OR REPLACE TABLE bronze_northwind.suppliers(SupplierID int, SupplierName STRING, ContactName STRING, Address STRING, City STRING, PostalCode STRING, Country STRING, Phone STRING, _metadata struct <file_name: STRING, file_size: LONG, file_moditication_time: TIMESTAMP,source_system: STRING, rows_written: INT, ingestion_type: STRING>) LOCATION 'abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/suppliers'" )

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED bronze_northwind.suppliers
