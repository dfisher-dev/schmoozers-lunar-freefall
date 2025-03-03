from backend_db_connector import DatabaseConnector
import freeFallNew

class DatabaseManager:
    def __init__(self, backend_db='backend.db'):
        self.db = DatabaseConnector(backend_db)
        self.db.connect()

    def create_new_mission(self, mass, altitude, start_fuel, thrust_power):
        query = '''
            INSERT INTO mission_start(mass, altitude, start_fuel, thrust_power)
            VALUES (?, ?, ?, ?)'''  # placeholders
        # Still need to figure out the above values
        self.db.execute_query(query, (mass, altitude, start_fuel, thrust_power))
        self.db.commit()
        print("New mission created")

    def get_mission_data(self, mission_id):
        # Retrieve mission data for a specific mission_id
        query = 'SELECT * FROM mission_data WHERE mission_id = ?'
        self.db.execute_query(query, (mission_id,))
        data = self.db.fetchall()
        print(data)  # Print the result to see what's being returned
        return data

    def update_mission_data(self, mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position):
        # Update mission data during the mission
        query = '''
            INSERT INTO mission_data (mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position)
            VALUES (?, ?, ?, ?, ?, ?, ?)'''  # more placeholders
        self.db.execute_query(query, (mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position))
        self.db.commit()
        print(f"Mission data updated for mission_id: {mission_id}")

    def close_connection(self):
        # Close database connection
        self.db.close()

manager = DatabaseManager()

# Create a new mission (with example values)
manager.create_new_mission(1500, 1000, 500, 75)

# Retrieve mission data (assuming mission ID is 1)
mission_data = manager.get_mission_data(1)
print(mission_data)  # Print the result of get_mission_data

# Close connection
manager.close_connection()