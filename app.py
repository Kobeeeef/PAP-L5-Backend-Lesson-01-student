# *** Complete Exercise 1 in pyreview.py in the python-review folder first ***

import sqlite3
from visualizer import display

# Exercise 2
# Import sqlite3
# Connect to the trees.db database
# Get a cursor, so you can write queries to the database

conn = sqlite3.connect("trees.db")
cursor = conn.cursor()

# Exercise 3
# Use the execute function to run a SELECT * query on trees.db
# Import the display function from visualizer.py
# Show the output of your select query on a webpage by using the display() function
# In the terminal, run this Python file
# Open tables.html with Live Server

cursor.execute("SELECT rowid, * FROM trees")
display(cursor)

# Exercise 4
# Edit the SELECT query to show the rowid 
# In the terminal, run this file again
# See the output of the query on tables.html
