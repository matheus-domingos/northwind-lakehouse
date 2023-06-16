# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql import *
from pyspark.sql.types import StructType

# COMMAND ----------

def add_metadata(df, source_system:str, ingestion_type: str):
    """Add a metadata struct on a DataFrame column

        Parameters: 
        df(DataFrame): The Dataframe based on raw data
        source_system(str): Source system of data in Raw
        ingestion_type(str): batch or streaming

        Returns:
        df(DataFrame): DataFrame containing raw data and a metadata column.
    """
    # drop unnecessary metadata
    df = df.withColumn("_metadata", col("_metadata").dropFields("file_path"))
    df = df.withColumn("_metadata", col("_metadata").dropFields("row_index"))

    # source system
    df = df.withColumn("source_system",lit(source_system.upper()))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("source_system"))))
    df = df.drop("source_system")
    
    # rows_written
    df = df.withColumn("rows_written",lit(df.count()))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("rows_written"))))
    df = df.drop("rows_written")

    # ingestion_type
    df = df.withColumn("ingestion_type",lit(ingestion_type))
    df = df.withColumn("_metadata", struct(col("_metadata.*"),(col("ingestion_type"))))
    df = df.drop("ingestion_type")

    return(df)
