# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.list(scope="DataLakeKeyVault")

# COMMAND ----------

application_id = dbutils.secrets.get(scope="DataLakeKeyVault",key="ad-app-id")
directory_id = dbutils.secrets.get(scope="DataLakeKeyVault",key="ad-app-directory-id")
storage_account_name = client_secret = dbutils.secrets.get(scope="DataLakeKeyVault",key="storage-account-name")
client_secret = dbutils.secrets.get(scope="DataLakeKeyVault",key="client-secret-app")


# COMMAND ----------

spark.conf.set(f"fs.azure.account.auth.type.{storage_account_name}.dfs.core.windows.net", "OAuth")
spark.conf.set(f"fs.azure.account.oauth.provider.type.{storage_account_name}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set(f"fs.azure.account.oauth2.client.id.{storage_account_name}.dfs.core.windows.net", application_id)
spark.conf.set(f"fs.azure.account.oauth2.client.secret.{storage_account_name}.dfs.core.windows.net", client_secret)
spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{storage_account_name}.dfs.core.windows.net", f"https://login.microsoftonline.com/{directory_id}/oauth2/token")

# COMMAND ----------

#service_credential = dbutils.secrets.get(scope="DataLakeKeyVault",key="fe8702c3-038c-4b75-8fd7-de763e18eb13")

spark.conf.set("fs.azure.account.auth.type.adlsnorthwinddataprd.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.adlsnorthwinddataprd.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.adlsnorthwinddataprd.dfs.core.windows.net", "60ddc046-9a3c-4d75-acbd-7a23ab20368f")
spark.conf.set("fs.azure.account.oauth2.client.secret.adlsnorthwinddataprd.dfs.core.windows.net", "1-a8Q~PuqX6XsHfB.PxlnptB2sN-92nzwSagdc26")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.adlsnorthwinddataprd.dfs.core.windows.net", "https://login.microsoftonline.com/66c31448-77b7-455e-919b-c54370919cf8/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls(f"abfss://raw@{storage_account_name}.dfs.core.windows.net/"))
