import sys

allData = open("6.in").read().split("\n")
allData = [ x.split(")") for x in allData ]
outerMost = ["YOU"]
connections = []
steps = -1

while(True):
    print(outerMost)
    for x in range(len(allData)):
        if(allData[x][0] in outerMost):
            connections.append(allData[x][1])
        if(allData[x][1] in outerMost):
            connections.append(allData[x][0])
    outerMost = connections
    connections = []
    if("SAN" in outerMost):
        print(steps)
        break
    steps += 1
