import sys

allData = open("6.in").read().split("\n")
allData = [ x.split(")") for x in allData ]
orbits = [["COM", 0]]
outerMost = ["COM"]
connections = []
layer = 1

while(True):    
    for x in range(len(allData)):
        if(allData[x][0] in outerMost):
            connections.append(allData[x][1])
    for x in range(len(connections)):
        orbits.append([connections[x], layer])
    layer += 1
    outerMost = connections
    connections = []
    if(len(orbits) - 1 == len(allData)):
        break

sum = 0
for x in range(len(orbits)):
    sum += orbits[x][1]
print(sum)
