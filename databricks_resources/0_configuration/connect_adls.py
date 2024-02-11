# Databricks notebook source
# getting secret values
application_id = dbutils.secrets.get(scope="DataLakeKeyVault",key="ad-app-id")
directory_id = dbutils.secrets.get(scope="DataLakeKeyVault",key="ad-app-directory-id")
storage_account_name = client_secret = dbutils.secrets.get(scope="DataLakeKeyVault",key="storage-account-name")
client_secret = dbutils.secrets.get(scope="DataLakeKeyVault",key="client-secret-app")

# COMMAND ----------

# configuring storage account access
spark.conf.set(f"fs.azure.account.auth.type.{storage_account_name}.dfs.core.windows.net", "OAuth")
spark.conf.set(f"fs.azure.account.oauth.provider.type.{storage_account_name}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set(f"fs.azure.account.oauth2.client.id.{storage_account_name}.dfs.core.windows.net", application_id)
spark.conf.set(f"fs.azure.account.oauth2.client.secret.{storage_account_name}.dfs.core.windows.net", client_secret)
spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{storage_account_name}.dfs.core.windows.net", f"https://login.microsoftonline.com/{directory_id}/oauth2/token")
