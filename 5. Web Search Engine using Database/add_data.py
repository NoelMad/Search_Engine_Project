import sqlite3

conn = sqlite3.connect("crawled_pages.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO pages (url, title, cleaned_content, pagerank)
VALUES (?, ?, ?, ?)
""", (
    "https://example.com",
    "Example Page",
    "flask sqlite search engine test data example",
    1.0
))

conn.commit()
conn.close()

print("✅ test data inserted")