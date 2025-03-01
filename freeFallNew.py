import math 
import time 
import os

h = int(input("How high is the lander form lunar surface (meters)?\n"))
print("starting position: ", h) 

#Need a system for evaluting graviational acceleration 
G = (6.67428e-11)       #grav constant
M = (7.34767309e22)     #mass of moon in kg
distance = h + 1737400 #point to point for 
g = -(G*M)/(distance*distance)

engineOn = False
fuelConsumptionRate = 1
velocity = 0
previousVelocity = 0
landerMassAmount = 1000
thrust = 1000
timeElapsed = 0
fuelRemaining = 3000
fuelMassConsumed = 10
fuelIncrement = 100
timeIncrement = 1

def newUpdateStats():
  global engineOn
  global fuelConsumptionRate
  global velocity
  global previousVelocity
  global landerMassAmount
  global thrust
  global timeElapsed
  global fuelRemaining
  global fuelMassConsumed
  global fuelIncrement
  global timeIncrement
  
  upwardAcceleration = thrust / landerMassAmount

  #velocity calculations
  if (engineOn == True) and (fuelRemaining != 0):
    velocity = velocity + (upwardAcceleration - G) * timeIncrement
    landerMass = landerMass - fuelMassConsumed
  else:
    velocity = velocity - G * timeIncrement
  
  fuelRemaining = fuelRemaining - (fuelIncrement * timeIncrement)
  timeElapsed = timeElapsed + timeIncrement


loops = 0
while (loops != 101):
  newUpdateStats()
  print(velocity)
  print(fuelRemaining)
  print(timeElapsed)
  print(landerMassAmount)
  loops = loops + 1