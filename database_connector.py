import sqlite3

class DatabaseConnector:
  def __init__(self, backend_db='backend.db'):
      self.backend_db = backend_db
      self.conn = None
      self.cursor = None

  def connect(self):
      # Establishes connection to database
      self.conn = sqlite3.connect(self.backend_db)
      self.cursor = self.conn.cursor()
      print("Database connection established")

  def close(self):
      # Closes database connection
      if self.conn:
          self.conn.close()
          print("Database connection closed")

  def commit(self):
      # Commit changes
      if self.conn:
          self.conn.commit()
          print("Changes committed to the database")

  def execute_query(self, query, params=()):
      # Run a query with parameters
        if self.cursor:
          self.cursor.execute(query, params)
          print(f"Executed query: {query}")

  def fetchall(self):
      # Fetch every row from the last query
      if self.cursor:
        return self.cursor.fetchall()

  def fetchone(self):
      # Fetch a row from the last query
      if self.cursor:
        return self.cursor.fetchone()
        
def get_mission_data():
  db = DatabaseConnector()
  db.connect()
  print("database connection successful")

    # Query to get latest mission data
  query = "SELECT mass, velocity, landerMass, start_fuel, thrust, fuelRemaining, altitude FROM mission_start ORDER BY mission_id DESC LIMIT 1"
  db.execute_query(query)
  mission_data = db.fetchone()

  db.close()
  print("database connection closed\n")

  if mission_data:
    # Print the mission data with line breaks
    print("Mission Data Retrieved:\n")
    print(f"\nMass: {mission_data[0]}")
    print(f"\nAltitude: {mission_data[1]}")
    print(f"\nStarting Fuel: {mission_data[2]}")
    print(f"\nThrust: {mission_data[3]}")
    print(f"\nVelocity: {mission_data[4]}")
    print(f"\nLander Mass: {mission_data[5]}")
    print(f"\nFuel Remaining: {mission_data[6]}")
    return {
      "mass": mission_data[0],
      "altitude": mission_data[1],
      "start_fuel": mission_data[2],
      "thrust": mission_data[3],
      "velocity": mission_data[4],
      "landerMass": mission_data[5],
      "fuelRemaining": mission_data[6]
    }
  else:
    print("No data found\n")
    return None

# Example usage:
"""
db = DatabaseConnector()
db.connect()
db.execute_query("SELECT thrust FROM mission_start")
results = db.fetchall()
print(results)
db.close()
"""