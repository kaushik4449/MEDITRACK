import sqlite3

DB_NAME = "meditrack.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            expiry_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database and medicines table ready!")


if __name__ == "__main__":
    create_table()