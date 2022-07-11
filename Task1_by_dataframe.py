import sqlite3
import pandas as pd

# Set the connection to get data from sqlite database
con = sqlite3.connect('_dataset/transactions.db')

# Get the data from sql tables as dataframes
df_devices = pd.read_sql_query("SELECT * from Devices", con)
df_transactions = pd.read_sql_query("SELECT * from Transactions", con)
df_sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", con)
df_sqlite_stat1 = pd.read_sql_query("SELECT * from sqlite_stat1", con)
df_sqlite_stat4 = pd.read_sql_query("SELECT * from sqlite_stat4", con)

# Close the connection of database after get the data
con.close()

# Group the visitors to find the total revenue that they created. Then sort these total revenue amounts
# and take maximum total revenue using head() function
most_revenue_visitor = df_transactions.groupby(['visitor_id'])['revenue'].sum().sort_values(ascending=False).head(1)
print("The Id of visitor created the most revenue is: ", most_revenue_visitor.index[0])
print("Total revenue from this visitor is: ", most_revenue_visitor.values[0])

# Creating copy of transaction dataframe and adding new column these dataframe to find net revenue without taxes.
df_copy = df_transactions.copy()
for index, row in df_copy.iterrows():
    current_tax = row['tax']
    current_revenue = row['revenue']
    df_copy.loc[index, 'revenue_without_tax'] = current_revenue/(1+current_tax)

# Group the visitors to find the net total revenue that they created. Then sort these net total revenue amounts
# and take maximum using head() function
visitor_without_tax = df_copy.groupby(['visitor_id'])['revenue_without_tax'].sum().sort_values(ascending=False).head(1)
print("\nThe Id of visitor created the most net revenue is: ", visitor_without_tax.index[0])
print("Net revenue from this visitor is without tax: ", visitor_without_tax.values[0])