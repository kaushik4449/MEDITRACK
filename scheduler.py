import sqlite3
from datetime import datetime, timedelta

DB_NAME = "meditrack.db"


def get_expiring_medicines(days=5):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    today = datetime.today().date()
    future_date = today + timedelta(days=days)

    cursor.execute("""
        SELECT name, expiry_date FROM medicines
        WHERE date(expiry_date) BETWEEN ? AND ?
        ORDER BY expiry_date
    """, (today.isoformat(), future_date.isoformat()))

    results = cursor.fetchall()
    conn.close()
    return results


def print_expiring_medicines():
    meds = get_expiring_medicines()

    if meds:
        print("⚠️ Medicines expiring soon:")
        for name, expiry in meds:
            print(f" - {name} (expires on {expiry})")
    else:
        print("✅ No medicines expiring in the next few days.")


if __name__ == "__main__":
    print_expiring_medicines()