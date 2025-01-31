import sqlite3

conn = sqlite3.connect('backend.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mission_start (
        mission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_height REAL,
        start_fuel REAL,
        thrust_power REAL,
        gravity REAL DEFAULT 1.62,
        time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')

conn.commit()
conn.close()
