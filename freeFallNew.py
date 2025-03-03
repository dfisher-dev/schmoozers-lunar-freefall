import math 
import time 
import os

height = int(input("How high is the lander form lunar surface (meters)?\n"))
print("starting position: ", height) 

#Need a system for evaluting graviational acceleration 
#G = (6.67428e-11)       #grav constant
G = (1.625)
M = (7.34767309e22)     #mass of moon in kg
distance = height + 1737400 #point to point for 
g = -(G*M)/(distance*distance)

engineOn = False
fuelConsumptionRate = 1
velocity = 0
previousVelocity = 0
landerMass = 1000
thrust = 3820
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
  global landerMass
  global thrust
  global timeElapsed
  global fuelRemaining
  global fuelMassConsumed
  global fuelIncrement
  global timeIncrement
  global height
  global landerMass

  upwardAcceleration = thrust / landerMass

  #height and velocity calculations
  if (engineOn == True) and (fuelRemaining != 0):
    height = height + velocity * timeIncrement - ((upwardAcceleration - G) * (timeIncrement ^ 2)) / 2
    velocity = velocity + (upwardAcceleration - G) * timeIncrement

    fuelRemaining = fuelRemaining - (fuelIncrement * timeIncrement)
    landerMass = landerMass - fuelMassConsumed
  else:
    height = height + velocity * timeIncrement - (G * (timeIncrement ^ 2)) / 2
    velocity = velocity - G * timeIncrement

  timeElapsed = timeElapsed + timeIncrement
  if (height <= 0):
    print("Lander has landed")


engineOn = True

loops = 0
while (loops != 300 and height > 0):
  newUpdateStats()
  print(velocity)
  print(fuelRemaining)
  print(timeElapsed)
  print(landerMass)
  print(height)
  print("-----")
  loops = loops + 1