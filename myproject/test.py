import sqlite3

conn = sqlite3.connect('/contacts.db')
cur = conn.cursor()
query = """INSERT INTO users VALUES(1, 'eleman', 'janybekov', '0553128256', 'eleman@gmail.com')"""
cur.execute(query)
conn.commit()
conn.close()
