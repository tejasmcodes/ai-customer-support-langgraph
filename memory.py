import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT
)
""")

conn.commit()


def save_query(query):
    cursor.execute(
        "INSERT INTO conversations(query) VALUES (?)",
        (query,)
    )
    conn.commit()


def get_previous_query():
    cursor.execute("""
    SELECT query
    FROM conversations
    ORDER BY id DESC
    LIMIT 2
    """)

    rows = cursor.fetchall()

    if len(rows) < 2:
        return "No previous conversation found."

    return rows[1][0]