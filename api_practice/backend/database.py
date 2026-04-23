import sqlite3

conn = sqlite3.connect('../db/data.db')

cursor = conn.cursor()

cursor.execute(""" \
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name VARCHAR,
age INTEGER,
height INTEGER
)
 """)