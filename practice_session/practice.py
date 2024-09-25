# Practice Session
# Exercise 1
# Import sqlite3
# Import display from visualizer.py
# Connect to the simplefolks database and get a cursor

import sqlite3
from visualizer import display

conn = sqlite3.connect("simplefolks.sqlite")
cursor = conn.cursor()


# Exercise 2
# There are 5 tables on the simplefolks database, we are going to run queries on:
# people, pets, politicians
# Run a separate SELECT all query on each table
# After each query, call the display function to show results on tables.html
# Open a terminal from the practice_session folder and run this file
# tables.html will auto-generate
# tables.html will only show the output from the last time you call display(), IOW, your last query
cursor.execute("SELECT rowid, * FROM people")
display(cursor)

cursor.execute("SELECT rowid, * FROM pets")
display(cursor)

cursor.execute("SELECT rowid, * FROM politicians")
display(cursor)


# Exercise 3
# Edit all 3 SELECT queries to show the rowid