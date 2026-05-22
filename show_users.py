import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "detections.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT id, email, password FROM users")
rows = cur.fetchall()
conn.close()

for row in rows:
    print(f"id={row[0]}, email={row[1]}, password={row[2]}")
