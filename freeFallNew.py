from database_connector import get_initial_mission_data
from database_connector import DatabaseConnector
import math 
import time 
import os
import backend_tables


def display_initial_mission_data():
  mission = get_initial_mission_data()

  if mission:
    velocity = mission["velocity"]
    landerMass = mission["mass"]
    thrust = mission["thrust"]
    fuelRemaining = mission["fuelRemaining"]
    altitude = mission["altitude"]

    print("Mission Data Retrieved:")
    print(f"Velocity: {velocity}")
    print(f"Lander Mass: {landerMass}")
    print(f"Thrust: {thrust}")
    print(f"Fuel Remaining: {fuelRemaining}")
    print(f"Altitude: {altitude}")

  else:
    print("Error: No mission data available")
    exit()



#Need a system for evaluting graviational acceleration 
#G = (6.67428e-11)       #grav constant
G = (1.625)
M = (7.34767309e22)     #mass of moon in kg

#distance = altitude + 1737400 #point to point for 
#g = -(G*M)/(distance*distance)

engineOn = False
fuelConsumptionRate = 1
previousVelocity = 0
fuelIncrement = 100
timeIncrement = 1

def newUpdateStats():
  global engineOn
  global fuelConsumptionRate
  global velocity
  global previousVelocity
  global landerMass
  global thrust
  global timeElapsed
  global fuelRemaining
  global fuelMassConsumed
  global fuelIncrement
  global timeIncrement
  global altitude
  global landerMass

  upwardAcceleration = thrust / landerMass

  #altitude and velocity calculations
  if (engineOn == True) and (fuelRemaining != 0):
    altitude = altitude + velocity * timeIncrement - ((upwardAcceleration - G) * (timeIncrement ^ 2)) / 2
    velocity = velocity + (upwardAcceleration - G) * timeIncrement

    fuelRemaining = fuelRemaining - (fuelIncrement * timeIncrement)
    landerMass = landerMass - fuelMassConsumed
  else:
    altitude = altitude + velocity * timeIncrement - (G * (timeIncrement ^ 2)) / 2
    velocity = velocity - G * timeIncrement

  timeElapsed = timeElapsed + timeIncrement
  if (altitude <= 0):
    print("Lander has landed\n")


engineOn = True

loops = 0
while (loops and altitude > 0):
  newUpdateStats()
  print(velocity)
  print(fuelRemaining)
  print(timeElapsed)
  print(landerMass)
  print(altitude)
  print("-----")
  loops = loops + 1

def create_new_mission(initial_height, initial_mass, initial_fuel):
  global landerMass
  global altitude
  global fuelRemaining
  
  backend_tables.createTables()

  db = DatabaseConnector()
  db.connect()
 
  # Insert mission data into the mission_start table
  query = '''
  INSERT INTO mission_start (mass, altitude, start_fuel, thrust, velocity)
  VALUES (?, ?, ?, ?, ?)'''
    
  # Assume altitude, fuel, and other values are set when creating the mission
  # altitude = float(input("Starting height?\n"))
  # landerMass = float(input("Mass of the schmoozer (kg's)?\n"))
  # start_fuel = float(input("Starting amount of fuel?\n"))
  
  altitude = initial_height
  landerMass = initial_mass
  start_fuel = initial_fuel

  fuelRemaining = start_fuel
  
  db.execute_query(query, (landerMass, altitude, start_fuel, thrust, velocity))

  db.commit()
  db.close()
  print("Mission created\n")

engineOn = True
fuelConsumptionRate = 10
velocity = 0
previousVelocity = 0
landerMass = 1000
thrust = 3000
timeElapsed = 0
fuelRemaining = 300
fuelIncrement = 5
fuelConsumptionRate = 10
timeIncrement = 1
altitude = 1000
fuelMassConsumed = 5



def run_mission_increment(engineIsOn):

  global engineOn
  global fuelConsumptionRate
  global velocity
  global previousVelocity
  global landerMass
  global thrust
  global timeElapsed
  global fuelRemaining
  global fuelMassConsumed
  global fuelIncrement
  global timeIncrement
  global altitude

  engineOn = engineIsOn

  db = DatabaseConnector()
  db.connect()
  print("database connection successful")

  newUpdateStats()

  query = '''
  INSERT INTO mission_data (time_stamp, altitude, fuel_remaining, mass, velocity, thrust_power)
  VALUES (?, ?, ?, ?, ?, ?)'''

  db.execute_query(query, (timeElapsed, altitude, fuelRemaining, landerMass, velocity, thrust))
  db.commit()
  active_mission_data = db.fetchone()
  print(active_mission_data)

  db.close()
  print("database connection closed\n")

  return [velocity, thrust, altitude, fuelRemaining]

def get_mission_data():
  db = DatabaseConnector()
  db.connect()
  print("database connection successful")

  query = '''
    SELECT * FROM mission_data'''
  db.execute_query(query)
  result = db.cursor.fetchall()
  print(result)
  

create_new_mission(1000, 1000, 1000)  # Set lander mass from user input
# display_initial_mission_data()
# run_mission_increment()
# get_mission_data()