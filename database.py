import sqlite3

conn = sqlite3.connect('challenge.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE tweet (
        tweet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tweet_kotor TEXT,
        tweet_bersih TEXT
)""")
conn.commit()
conn.close()
