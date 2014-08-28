# Create a SQLite3 database and table


# import the SQLite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 820000)")
cursor.execute("INSERT INTO population VALUES('San Francisco City', 'NY', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()