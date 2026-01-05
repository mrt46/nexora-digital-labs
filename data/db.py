# data/db.py

import sqlite3

def get_conn():
    return sqlite3.connect("data/trend_intel.db")

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS trend_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        region TEXT,
        site TEXT,
        topic TEXT,
        traffic_level TEXT,
        velocity TEXT,
        adaptability TEXT,
        risk_level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
