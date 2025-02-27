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

print(g)


void = input("Press enter to start the simulation\n")
seconds = time.time()

position = h
#all the while loop does is replace the console with the most up to date number, not permanant 
while position>0:
  elapsed_time = time.time() - seconds
  v0 = 0#initial velocity is zero
  v = v0 + g*elapsed_time
  position = h + v0*(elapsed_time) + (g*(elapsed_time)*(elapsed_time))/2
  os.system('clear')
  
  print("Position: ", position)
  print("Velocity: ", v)


initialHeight = h
initialVelocity = 0
timeIncrement = 1
thrust = 1000
previousLanderMass = 3000
moonRadius = 1740000

# Update statistics
def updateStats():
  currentHeight = initialHeight
  previousVelocity = initialVelocity
  while (currentHeight > 0):
    # gravitational acceleration of lander relative to height (h) of lander
    gravAccelAtCurrentHeight = (G*M)/(moonRadius+currentHeight)^2
    
    # net average acceleration at time (t)
    currentNetAvgAccel = (thrust - gravAccelAtCurrentHeight*previousLanderMass)/(previousLanderMass-(0.5)*currentFuelMass)
    
    velocity = previousVelocity + currentNetAvgAccel*timeIncrement
    
    previousFuelMass = fuelMass
    previousVelocity = velocity

def updateWithThrusters():
  currentAcceleration = (thrustForce - gravAccelAtCurrentHeight * previousLanderMass - (0.5) * massOfFuel)
  heightAfterThrust = previousHeight - previousVelocity * timeIncrement - (0.5) * currentAcceleration * timeIncrement^2
