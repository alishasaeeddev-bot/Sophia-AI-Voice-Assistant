import sqlite3

con = sqlite3.connect("sophia.db")
cursor = con.cursor()

# Insert system commands
commands = [
    ("notepad", "C:\\Windows\\System32\\notepad.exe"),
    ("calculator", "C:\\Windows\\System32\\calc.exe"),
    ("chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
]

for name, path in commands:
    cursor.execute("INSERT INTO sys_command(name, path) VALUES (?, ?)", (name, path))

con.commit()
con.close()
print("System commands inserted!")