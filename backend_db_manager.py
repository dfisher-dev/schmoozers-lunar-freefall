from backend_db_connector import DatabaseConnector

class DatabaseManager:
    def __init__(self, backend_db='backend.db'):
        self.db = DatabaseConnector(backend_db)
        self.db.connect()

    def create_new_mission(self, mass, altitude, start_fuel, thrust_power):
        """Insert a new mission's initial data into mission_start."""
        query = '''
            INSERT INTO mission_start (mass, altitude, start_fuel, thrust_power)
            VALUES (?, ?, ?, ?)'''
        self.db.execute_query(query, (mass, altitude, start_fuel, thrust_power))
        self.db.commit()
        print("New mission created.")

    def get_mission_data(self, mission_id):
        """Retrieve mission data for a specific mission_id."""
        query = 'SELECT * FROM mission_data WHERE mission_id = ?'
        self.db.execute_query(query, (mission_id,))
        return self.db.fetchall()

    def update_mission_data(self, mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position):
        """Update mission data during the mission."""
        query = '''
            INSERT INTO mission_data (mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position)
            VALUES (?, ?, ?, ?, ?, ?, ?)'''
        self.db.execute_query(query, (mission_id, altitude, fuel_remaining, velocity, mass, thrust_power, position))
        self.db.commit()
        print(f"Mission data updated for mission_id: {mission_id}")

    def close_connection(self):
        """Close the database connection."""
        self.db.close()

# Example usage:
# manager = DatabaseManager()
# manager.create_new_mission(1500, 1000, 500, 75)
# mission_data = manager.get_mission_data(1)
# print(mission_data)
# manager.update_mission_data(1, 900, 480, 200, 1450, 80, 100)
# manager.close_connection()