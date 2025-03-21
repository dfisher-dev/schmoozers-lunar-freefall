from database_connector import get_initial_mission_data
from database_connector import DatabaseConnector
import math 
import time 
import os

mission = get_initial_mission_data()

if mission:
  velocity = mission["velocity"]
  landerMass = mission["mass"]
  thrust = mission["thrust"]
  fuelRemaining = mission["fuelRemaining"]
  altitude = mission["altitude"]

  print("\nMission Data Retrieved:")
  print("-" * 50)
  print(f"Velocity        : {velocity:.2f} m/s")
  print(f"Lander Mass     : {landerMass:.2f} kg")
  print(f"Thrust          : {thrust:.2f} N")
  print(f"Fuel Remaining  : {fuelRemaining:.2f} kg")
  print(f"Altitude        : {altitude:.2f} meters")
  print("-" * 50)

else:
  print("Error: No mission data available")
  exit()

#Need a system for evaluting graviational acceleration 
#G = (6.67428e-11)       #grav constant
G = (1.625)
M = (7.34767309e22)     #mass of moon in kg

distance = altitude + 1737400 #point to point for 
g = -(G*M)/(distance*distance)

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

  timeElapsed = 0

  upwardAcceleration = thrust / landerMass

  fuelMassConsumed = fuelConsumptionRate * fuelIncrement * timeIncrement

  #altitude and velocity calculations
  if (engineOn == True) and (fuelRemaining != 0):
    altitude = altitude + velocity * timeIncrement - ((upwardAcceleration - G) * (timeIncrement ** 2)) / 2
    velocity = velocity + (upwardAcceleration - G) * timeIncrement

    fuelRemaining = fuelRemaining - (fuelIncrement * timeIncrement)
    landerMass = landerMass - fuelMassConsumed
  else:
    altitude = altitude + velocity * timeIncrement - (G * (timeIncrement ** 2)) / 2
    velocity = velocity - G * timeIncrement

  timeElapsed = timeElapsed + timeIncrement
  if (altitude <= 0):
    print("Lander has landed\n")


engineOn = True

loops = 0
while (altitude > 0):
  newUpdateStats()
  print(velocity)
  print(fuelRemaining)
  print(timeElapsed)
  print(landerMass)
  print(altitude)
  print("-----")
  loops = loops + 1

def create_new_mission(fuelRemaining=500.0, thrust=75.0, velocity=110.0, gravity=1.62):
  db = DatabaseConnector()
  db.connect()
 
  # Insert mission data into the mission_start table
  query = '''
  INSERT INTO mission_start (mass, altitude, start_fuel, thrust, velocity, fuelRemaining)
  VALUES (?, ?, ?, ?, ?, ?)'''
    
  while True:
    try:
      altitude = float(input("Enter starting altitude (in meters): "))
      landerMass = float(input("Enter mass of the schmoozer (in kg): "))
      start_fuel = float(input("Enter starting amount of fuel (in kg): "))
      break
    except ValueError:
      print("Invalid input. Please enter valid numeric values.")
  
  db.execute_query(query, (landerMass, altitude, start_fuel, thrust, velocity, fuelRemaining))

  db.commit()
  db.close()
  print("Mission created\n")

# Example usage:
  # Set lander mass from user input

# get_initial_mission_data()

def run_mission():

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
  global time_stamp

  db = DatabaseConnector()
  db.connect()
  print("database connection successful")

  time_stamp = 0
  timeElapsed = 0

  while (altitude > 0):

    newUpdateStats()

    time_stamp += timeIncrement
    timeElapsed += timeIncrement

    query = '''
      INSERT INTO mission_data (time_stamp, velocity, previousVelocity, mass, thrust, timeElapsed, fuelRemaining, fuelMassConsumed, fuelIncrement, timeIncrement)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    db.execute_query(query, (time_stamp, velocity, previousVelocity, landerMass, thrust, timeElapsed, fuelRemaining, fuelMassConsumed, fuelIncrement, timeIncrement))
    
    db.commit()

    print(f"Inserted data for time {timeElapsed}: Velocity = {velocity}, Altitude = {altitude}, Fuel Remaining = {fuelRemaining}")

    time.sleep(1)

  db.close()
  print("database connection closed\n")

run_mission()