from pyspark.sql.functions import col, lit, struct

def add_metadata_save(df, batchId, source_name = 'source'):
    """Add a metadata struct on a DataFrame column

        Parameters: 
        df(DataFrame): DataFrame with raw data
        batchId: Id of micro-batch

    """
    
    # removing unecessary columns
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

    df.write.mode("append").format("delta").saveAsTable(f"bronze_northwind.{source_name}")