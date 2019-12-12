import sys
import re

allData = open("12.in").read().split("\n")
positions = [re.sub("[^0-9,-]", "", x).split(",") for x in allData]
positions = [[int(str(j)) for j in i] for i in positions]
velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

steps = 0
x = 0
y = 0
z = 0
while(x == 0 or y == 0 or z == 0):
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
    
    steps += 1
    print("pos:" + str(positions))
    print("vel:" + str(velocities))
    print("steps:" + str(steps))    
    if(velocities[0][0] == 0 and velocities[1][0] == 0 and velocities[2][0] == 0 and velocities[3][0] == 0):
        x = steps
    if(velocities[0][1] == 0 and velocities[1][1] == 0 and velocities[2][1] == 0 and velocities[3][1] == 0):
        y = steps
    if(velocities[0][2] == 0 and velocities[1][2] == 0 and velocities[2][2] == 0 and velocities[3][2] == 0):
        z = steps
    print("x:" + str(x) + " y:" + str(y) + " z:" + str(z))

def lcm(denominators):
    import math
    import functools
    return functools.reduce(lambda a,b: a*b // math.gcd(a,b), denominators)
print(lcm([x, y, z]) * 2)
