import sqlite3
import pandas as pd

# Set the connection to get data from sqlite database
con = sqlite3.connect('_dataset/transactions.db')

# Nested query to group the day from datetime column and calculate the total revenue created on this day 
# Then find the maximum revenue of these total revenue for this day
query2 = pd.read_sql('''SELECT  day,  MAX(total_revenue)
               FROM (SELECT strftime('%d',datetime) as day, SUM(revenue) as total_revenue
               FROM Transactions
               WHERE device_type = 3
               GROUP BY strftime('%d',datetime))''', con)

print("The day of the most revenue and revenue for users who ordered via a mobile phone was created is:\n ",  query2)

# Close the connection of database after get the data
con.close()