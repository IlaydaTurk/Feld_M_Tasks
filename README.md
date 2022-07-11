# Feld M Tasks

## Data Used

-   Data: Transactions.db
-   The Currency Conversion Rates File: eurofxref-hist-90d.xml

## Libraries Used

   sqlite3
   pandas
   datetime
   xml.etree.ElementTree as ET
   psycopg2
 
### 1. Task1
For Task 1, I tried to find the visitor who created the most revenue by pandas data frame operations and by SQL commands.
As a first, I took the transactions and devices tables data as data frames.

- In the *Task1_by_dataframe* file, I grouped the visitors to find the total revenue that they created. Then I sorted these total revenue as descending and took the maximum total revenue and the id of visitor that created this revenue.
Also, I calculated the most net revenue by dropping tax and it gave the same visitor_id.

- In the *Task1_by_sql* file, I find the visitor who created the most revenue by using SQL commands. I used nested queries to group visitor_id's and calculate the total revenue that they created. Then I returned the maximum total revenue and the id of the visitor that created this revenue.

### 2. Task2
In Task 2, I tried to find the day when the most revenue was created by mobile phones using pandas data frame operations and SQL commands.

- In the *Task2_by_dataframe* file, after I took the transaction and devices data from the database, I checked columns' data types and updated them to be able to work on DateTime data. I used pandas data frame mask operations to find only transactions created by mobile phones and then grouped the total revenues by day from datetime column and took the maximum total revenue using the head function after sorting as descending them.

- In the *Task2_by_sql* file, I used strftime function to get the day from datetime column from the transaction table then in the nested query, took only transactions created by mobile phone using the where command and also used the sum aggregation function to sum revenues according to the days. As a last, I got the maximum total revenue and the day when the most total revenue was created by mobile phone.

### 3. Task3

In the *Task3* file, after I took the tables as data frames from the database, merged transactions and devices tables using their common column which is device_id for transactions and id for device table. After that, I dropped one of the device_id columns to the merged data frame to contain one device id column and using pandas stored them on a new .csv file.

### 4. Task4
In the *Task4* file, I took the transactions data as in previous tasks and also an XML file to take currency rates. To parse XML file, I used "xml.etree.ElementTree" module. Since I only need the date of the currency changes and the equivalent of the USD rates on that date, I looped through the XML that I parsed, got the dates of the currency changes and the equivalent currency rate of the USD rates on that date, and stored them as the 'time' and 'currency_rate' columns in the new dataframe. 
Then, I converted these dates to EUR by comparing the dates of the transaction with the loop in the transaction dataframe. Since the dataframe I created from XML does not contain all the dates in the transaction dataframe, I used the currency rate of the closest date, which is before than the date of the transaction, for the dates that do not exist.

### 5. Task5

In the *Task5* fileAfter getting the data from the database as a dataframes , I created a new database connection with PostgreSQL and added the transaction and devices dataframes to the PostgreSQL database as tables. Then I reassigned Foreign Key and Primary Keys so that the Transaction and Devices tables could be linked using SQL commands.