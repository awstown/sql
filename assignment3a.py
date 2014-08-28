# Assignment 3a - insert random data

# import libraries
import sqlite3
import random

# establish connection to database
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # create tables numbers and (add a drop so we can run again and again)
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")

    # Use a for loop to in insert 100 random numbers
    for i in range(100):
        c.execute("INSERT INTO numbers VAULES (?)", (random.randint(0, 100),))
