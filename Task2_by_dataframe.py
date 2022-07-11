import sqlite3
import pandas as pd
import datetime

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

# Change the type of datetime column as datetime 
df_transactions['datetime'] = df_transactions['datetime'].astype('datetime64[ns]')
# Mask the transaction dataframe to find visitors used mobile phone
masked_df = df_transactions[df_transactions['device_type'] == 3]
# Grouping the day from datetime column and calculate the total revenue created on this day
# and take maximum total revenue using head() function
most_revenue_day = masked_df.groupby(masked_df['datetime'].dt.day)['revenue'].sum().sort_values(ascending=False).head(1)

print("The day of the most revenue for users who ordered via a mobile phone was created is: ", most_revenue_day.index[0])
print("Revenue for this day is: ", most_revenue_day.values[0])