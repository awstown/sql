# Create a SQLite3 database and table


# import the SQLite3 library
import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 820000)")
    c.execute("INSERT INTO population VALUES('San Francisco City', 'NY', 800000)")
