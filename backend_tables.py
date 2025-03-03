import sqlite3
import freeFallNew

conn = sqlite3.connect('backend.db')
cursor = conn.cursor()

# Function to create mission_start table in backend.db - pre mission values
# Need to double check table values
cursor.execute('''CREATE TABLE IF NOT EXISTS mission_start(
        mission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_time REAL,
        time_start REAL,
        time_passed REAL,
        mass REAL,
        velocity REAL,    
        altitude REAL,
        start_fuel REAL,
        thrust_power REAL,
        gravity REAL DEFAULT 1.62
    )''')

# Commits the table to the database before moving to the next one
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mission_data(
        data_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mission_id INTEGER,
        time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        altitude REAL,
        fuel_remaining REAL,
        velocity REAL,
        mass REAL,
        thrust_power REAL,
        position REAL,
        FOREIGN KEY (mission_id) REFERENCES mission_start (mission_id)
    )''')

conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mission_outputs(
        output_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mission_id INTEGER,
        success BOOLEAN,
        final_velocity REAL,
        final_altitude REAL,
        fuel_used REAL,
        landing_time REAL,
        remarks TEXT,
        FOREIGN KEY (mission_id) REFERENCES mission_start (mission_id)
    )''')

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()
print("Tables in the database:", tables)

conn.close()

