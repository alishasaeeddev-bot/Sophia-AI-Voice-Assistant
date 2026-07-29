import sqlite3

con = sqlite3.connect("sophia.db")
cursor = con.cursor()

# Insert web commands
web_commands = [
    ("youtube", "https://www.youtube.com"),
    ("google", "https://www.google.com"),
    ("canva", "https://www.canva.com"),
    ("facebook", "https://www.facebook.com"),
    ("wattsapp", "https://web.whatsapp.com/"),
    ("twitter", "https://www.twitter.com"),
    ("geo news", "https://www.geo.tv/"),
    ("ary news", "https://arynews.tv/"),
    ("dawn", "https://www.dawn.com/"),
    ("express news", "https://www.express.pk/"),
    ("samaa news", "https://www.samaa.tv/")
]


for name, url in web_commands:
    cursor.execute("INSERT INTO web_command(name, url) VALUES (?, ?)", (name, url))

con.commit()
con.close()
print("Web commands inserted!")