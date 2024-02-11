# Databricks notebook source
# MAGIC %run ../0_configuration/connect_adls

# COMMAND ----------

import sys
sys.path.append("/Workspace/Repos/matheus.domingos@live.com/northwind-lakehouse/databricks_resources/0_configuration")
from functions import add_metadata_save

# COMMAND ----------

# defining variables
process_source_name = dbutils.widgets.get("process_source_name")
file_path = f"abfss://landingzone@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}"
table_path = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}"
schema_location = f"abfss://control@{storage_account_name}.dfs.core.windows.net/northwind/schemas/{process_source_name}"
bronze_northwind_path = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind"

# COMMAND ----------

# reading, adding metadata and saving data from landingzone to bronze layer
streaming_df = (spark
    .readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", schema_location)  
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
    .load(file_path)
    .select("*", "_metadata")
)

streaming_query = (streaming_df
    .writeStream
    .format("delta")
    .trigger(availableNow=True)
    #.foreachBatch(add_metadata_save) # to add more metadata or apply any other transformation + saving the data
    .outputMode("append")
    .option("checkpointLocation", f"abfss://control@{storage_account_name}.dfs.core.windows.net/northwind/checkpoints/{process_source_name}/")
    #.start(f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}/") # for loading external tables
    .toTable(f"prd_bronze.bronze_northwind.{process_source_name}") # for creating and loading managed tables
)

streaming_query.awaitTermination()

# COMMAND ----------

dbutils.notebook.exit("Success")
