import sys
import re

allData = open("12.in").read().split("\n")
positions = [re.sub("[^0-9,-]", "", x).split(",") for x in allData]
positions = [[int(str(j)) for j in i] for i in positions]
velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
upperLimit = 1000

def gravity(planet1, planet2):
    global positions
    global velocities
    xyz = 0
    while(xyz < 3):
        if(positions[planet1][xyz] < positions[planet2][xyz]):
            velocities[planet1][xyz] += 1
            velocities[planet2][xyz] -= 1
        elif(positions[planet1][xyz] > positions[planet2][xyz]):
            velocities[planet1][xyz] -= 1
            velocities[planet2][xyz] += 1
        xyz += 1
for x in range(upperLimit):
    gravity(0, 1)
    gravity(0, 2)
    gravity(0, 3)
    gravity(1, 2)
    gravity(1, 3)
    gravity(2, 3)

    positions[0][0] += velocities[0][0]
    positions[0][1] += velocities[0][1]
    positions[0][2] += velocities[0][2]

    positions[1][0] += velocities[1][0]
    positions[1][1] += velocities[1][1]
    positions[1][2] += velocities[1][2]
    
    positions[2][0] += velocities[2][0]
    positions[2][1] += velocities[2][1]
    positions[2][2] += velocities[2][2]
    
    positions[3][0] += velocities[3][0]
    positions[3][1] += velocities[3][1]
    positions[3][2] += velocities[3][2]
    print("pos:" + str(positions))
    print("vel" + str(velocities))

totalEnergy = 0
potEnergy = abs(positions[0][0]) + abs(positions[0][1]) + abs(positions[0][2])
kinEnergy = abs(velocities[0][0]) + abs(velocities[0][1]) + abs(velocities[0][2])
totalEnergy += potEnergy * kinEnergy
potEnergy = abs(positions[1][0]) + abs(positions[1][1]) + abs(positions[1][2])
kinEnergy = abs(velocities[1][0]) + abs(velocities[1][1]) + abs(velocities[1][2])
totalEnergy += potEnergy * kinEnergy
potEnergy = abs(positions[2][0]) + abs(positions[2][1]) + abs(positions[2][2])
kinEnergy = abs(velocities[2][0]) + abs(velocities[2][1]) + abs(velocities[2][2])
totalEnergy += potEnergy * kinEnergy
potEnergy = abs(positions[3][0]) + abs(positions[3][1]) + abs(positions[3][2])
kinEnergy = abs(velocities[3][0]) + abs(velocities[3][1]) + abs(velocities[3][2])
totalEnergy += potEnergy * kinEnergy
print(totalEnergy)
