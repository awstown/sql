# Assignment 3b - prompt the user

# import the sqlite3 lib
import sqlite3

# create the connection object
conn = sqlite3.connect("newnum.db")

# create cursor object used to execute SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until user enters a valid operation number [1-5]
while True
    # get user input
    x = raw_input(prompt)

    ........
