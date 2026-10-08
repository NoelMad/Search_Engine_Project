import sqlite3

conn = sqlite3.connect("crawled_pages.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    title TEXT,
    cleaned_content TEXT,
    pagerank REAL
)
""")

conn.commit()
conn.close()

print("✅ pages table created")