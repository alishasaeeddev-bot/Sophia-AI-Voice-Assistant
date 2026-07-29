import sqlite3

conn = sqlite3.connect("sophia.db")

cursor = conn.cursor()
query = "OneNote"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
results = cursor.fetchall()
print(results[0][0])