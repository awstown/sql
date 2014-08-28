# INSERT Command with Error Handler

# import the sqlite3 lib
import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    # insert data
    cursor.execute(
        "INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute(
        "INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again..."

# close the database connection
conn.close()
