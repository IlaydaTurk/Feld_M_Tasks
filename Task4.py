import xml.etree.ElementTree as ET
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

# Parse the currency conversion rates xml file
tree = ET.parse('_dataset/eurofxref-hist-90d.xml')
root = tree.getroot()

# Create new dataframe to store xml file attributes
df_cols = ["time", "rate"]
rows = []

# Take USD currency rates according to their exchange times and store them on exchange dataframe
for child in root:
    for subchild in child: 
        for subsubchild in subchild:
            if subsubchild.attrib['currency'] == "USD":
                time_col = subchild.attrib.get('time')
                cur_rate = subsubchild.attrib['rate']
                rows.append({"time": time_col,
                             "rate":cur_rate })
# Create exchange dataframe from USD currency rates and their exchange time
exchange_df = pd.DataFrame(rows, columns = df_cols)
# Change dtypes for rate and time column of exchange dataframe
exchange_df.rate.astype(float)
exchange_df['time'] = pd.to_datetime(exchange_df['time'])
print("Transaction dataframe before convert USD to EUR:\n", df_transactions.head(10))

# Update the revenues in EUR instead of USD in the transaction dataframe.
# For the dates that are not in the xml file, the exchange currency rate of 
# the closest and the smallest maximum date to that date from that date is taken as a basis.
for index, row in df_transactions.iterrows():
    current_time = row['datetime']
    mask = exchange_df[exchange_df['time'] <= current_time].max()
    rate = mask['rate']
    df_transactions.loc[index, 'revenue'] = row['revenue']/float(rate)

print("\nTransaction dataframe after convert USD to EUR:\n", df_transactions.head(10))