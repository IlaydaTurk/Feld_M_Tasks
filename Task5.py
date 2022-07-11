import psycopg2
from psycopg2 import Error
import sqlite3
import pandas as pd

# Set the connection to get data from sqlite database
con = sqlite3.connect('_dataset/transactions.db')
cursor_1 = con.cursor()

# Get the data from sql tables as dataframes
df_devices = pd.read_sql_query("SELECT * from Devices", con)
df_transactions = pd.read_sql_query("SELECT * from Transactions", con)
df_sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", con)
df_sqlite_stat1 = pd.read_sql_query("SELECT * from sqlite_stat1", con)
df_sqlite_stat4 = pd.read_sql_query("SELECT * from sqlite_stat4", con)
# Close the connection of database after get the data
con.close()

# Add support for postresql database
try:
    # Set the connection to insert data to postgreSQL database
    conn = psycopg2.connect(
       database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Add transactions and devices dataframes to database as tables
    # if_exists='replace' patameter to update old table
    df_transactions.to_sql('Transactions', con=conn, if_exists='replace', index = False)
    df_devices.to_sql('Devices', con=conn, if_exists='replace', index = False)

    # Set primary keys and foreign key for Transactions and Devices Tables
    query1 = '''ALTER TABLE Transactions
                ADD PRIMARY KEY (id);'''

    query2 = '''ALTER TABLE Devices
                ADD PRIMARY KEY (id);'''

    query3 = '''ALTER TABLE Transactions
                ADD CONSTRAINT fk_device_id FOREIGN KEY (device_type) 
                REFERENCES Devices (id);'''
    # Execute queries
    cursor.execute(query1)
    conn.commit()
    print("Primary Key updated Transactions Table for in PostgreSQL ")
    cursor.execute(query2)
    conn.commit()
    print("Primary Key updated Devices Table for in PostgreSQL ")
    cursor.execute(query3)
    conn.commit()
    print("Foreign Key updated Transactions Table for in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")