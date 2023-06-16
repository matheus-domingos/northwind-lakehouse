# Databricks notebook source
# MAGIC %run ../0_configuration/connect_adls

# COMMAND ----------

# MAGIC %run ../0_configuration/shared_functions

# COMMAND ----------

# imports
from pyspark.sql.types import StructType, StructField, TimestampType, IntegerType, StringType, LongType
from pyspark.sql.functions import *
from pyspark.sql import *

# COMMAND ----------

# enable automerge for schema
spark.sql("SET spark.databricks.delta.schema.autoMerge.enabled = true")

# COMMAND ----------

# defining variables
# process_source_name = dbutils.widgets.get("process_source_name")
process_source_name = 'suppliers'
file_path = f"abfss://landingzone@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}"
table_path = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}"
schema_location = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/schemas/{process_source_name}"
bronze_northwind_path = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind"

# COMMAND ----------

# defining function for transforming and saving data on writeStream
def add_metadata_save(df, batchId):
    """Add a metadata struct on a DataFrame column

        Parameters: 
        df(DataFrame): DataFrame with raw data
        batchId: Id of micro-batch

    """
    # removing unecessary coluns
    df = df.withColumn("_metadata", col("_metadata").dropFields("file_path"))
    df = df.withColumn("_metadata", col("_metadata").dropFields("row_index"))

    # source system
    df = df.withColumn("source_system",lit("northwind"))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("source_system"))))
    df = df.drop("source_system")
    
    # rows_written
    df = df.withColumn("rows_written",lit(df.count()))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("rows_written"))))
    df = df.drop("rows_written")

    # ingestion_type
    df = df.withColumn("ingestion_type",lit("batch"))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("ingestion_type"))))
    df = df.drop("ingestion_type")

    df.write.mode("append").format("delta").saveAsTable(f"bronze_northwind.{process_source_name}")

# COMMAND ----------

# reading, adding metadata and saving data from landingzone in bronze layer
df = (spark
    .readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", f"{schema_location}")  
    .option("cloudFiles.schemaEvolutionMode","addNewColumns")
    .load(file_path)
    .select("*","_metadata")

    .writeStream
    .format("delta")\
    .foreachBatch(add_metadata_save)
    .trigger(availableNow=True)\
    .option("checkpointLocation", f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/checkpoints/{process_source_name}/")\
    .start(f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/northwind/{process_source_name}/")
)

# COMMAND ----------

df = (spark
    .readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", f"{schema_location}")  
    .option("cloudFiles.schemaEvolutionMode","addNewColumns")
    .load(file_path)
    .select("*","_metadata"))

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze_northwind.shippers

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`abfss://bronze@adlsnorthwinddataprd.dfs.core.windows.net/northwind/shippers`

# COMMAND ----------

dbutils.notebook.exit("Success")
