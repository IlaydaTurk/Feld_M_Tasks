import sqlite3
import pandas as pd

# Set the connection to get data from sqlite database
con = sqlite3.connect('_dataset/transactions.db')
cursor = con.cursor()

# Get the data from sql tables as dataframes
df_devices = pd.read_sql_query("SELECT * from Devices", con)
df_transactions = pd.read_sql_query("SELECT * from Transactions", con)
df_sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", con)
df_sqlite_stat1 = pd.read_sql_query("SELECT * from sqlite_stat1", con)
df_sqlite_stat4 = pd.read_sql_query("SELECT * from sqlite_stat4", con)

# Close the connection of database after get the data
con.close()

# Rename id column of devices dataframe to prevent conflict of id column for transactions dataframe
df_devices.rename(columns = {'id':'id_devices'}, inplace = True)
# Merge transactions and devices dataframes 
# then drop id_devices column so that the merged dataframe doesn't have two identical columns for device id
merged_df = pd.merge(df_transactions, df_devices, left_on="device_type", right_on="id_devices").drop('id_devices', axis=1).sort_values('id')
# Store merged dataframe on sinfle flat file
merged_df.to_csv('_dataset/transactions_devices_merged.csv', index = False)
