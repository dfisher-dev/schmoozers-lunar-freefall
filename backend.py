import sqlite3

conn = sqlite3.connect('backend.db')
cursor = conn.cursor()

# Function to create mission_start table in backend.db - pre mission values
# Need to double check table values
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS mission_start (
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
    );
''')

# Commits the table to the database before moving to the next one
conn.commit()

# Table to store values during the mission
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mission_data (
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
    );
''')

# Commit the table and close it
conn.commit()
conn.close()

'''Consider total time, altitude, mass, velocity, 
time and time passed, time Impact

Going to need a database manager and connector as well

Need to meet with everyone in or to integrate the backend properly'''