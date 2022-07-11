import sqlite3
import pandas as pd

# Set the connection to get data from sqlite database
con = sqlite3.connect('_dataset/transactions.db')

# Nested query to group the visitors to find the total revenue that they created. 
# Then find the maximum revenue of these total revenue amounts
query1 = pd.read_sql('''SELECT visitor_id, MAX(total_revenue)
                        FROM (SELECT visitor_id, SUM(revenue) as total_revenue
                              FROM Transactions
                              GROUP BY visitor_id)''', con)

print("The Id and revenue of visitor created the most revenue is:\n ", query1)

# Close the connection of database after get the data
con.close()