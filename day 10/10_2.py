import sys
import math
import copy
from operator import itemgetter
allData = [list(x) for x in open("10.in").read().split("\n")]

currentTest = [22, 19]

testCase = [0, 0]
while(currentTest[1] < len(allData)):
    if(allData[currentTest[1]][currentTest[0]] == "#"):
        grid = [list(x) for x in open("10.in").read().split("\n")]
        testCase = [0, 0]
        while(testCase[1] < len(grid)):
            if(grid[testCase[1]][testCase[0]] == "#" and testCase != currentTest):
                #find slope of line
                if(currentTest[0] - testCase[0] != 0 and currentTest[1] - testCase[1] != 0):
                    slope = [currentTest[1] - testCase[1], currentTest[0] - testCase[0]]
                    simplify = abs(math.gcd(slope[0], slope[1]))
                    if(simplify != 1):
                        slope[0] = int(slope[0] / simplify)
                        slope[1] = int(slope[1] / simplify)
                elif(currentTest[0] - testCase[0] == 0):
                    #vertitcal line
                    if(testCase[1] < currentTest[1]):
                        slope = "vertically up"
                    else:
                        slope = "vertically down"
                elif(currentTest[1] - testCase[1] == 0):
                    #horizontal line
                    if(testCase[0] < currentTest[0]):
                        slope = "horizontally left"
                    else:
                        slope = "horizontally right"
                posInPath = []
                comparePos = copy.copy(currentTest)
                seenAsteroid = False
                if(isinstance(slope, str) == True):
                    if(slope == "horizontally right"):
                        comparePos[0] += 1
                        while(comparePos[0] < len(grid[0])):
                            if(grid[comparePos[1]][comparePos[0]] == "#"):
                                if(seenAsteroid == False):
                                    grid[comparePos[1]][comparePos[0]] = "O"
                                    seenAsteroid = True
                                else:
                                    grid[comparePos[1]][comparePos[0]] = "X"
                            comparePos[0] += 1
                    elif(slope == "horizontally left"):
                        comparePos[0] -= 1
                        while(comparePos[0] >= 0):
                            if(grid[comparePos[1]][comparePos[0]] == "#"):
                                if(seenAsteroid == False):
                                    grid[comparePos[1]][comparePos[0]] = "O"
                                    seenAsteroid = True
                                else:
                                    grid[comparePos[1]][comparePos[0]] = "X"
                            comparePos[0] -= 1
                    elif(slope == "vertically down"):
                        comparePos[1] += 1
                        while(comparePos[1] < len(grid)):
                            if(grid[comparePos[1]][comparePos[0]] == "#"):
                                if(seenAsteroid == False):
                                    grid[comparePos[1]][comparePos[0]] = "O"
                                    seenAsteroid = True
                                else:
                                    grid[comparePos[1]][comparePos[0]] = "X"
                            comparePos[1] += 1
                    elif(slope == "vertically up"):
                        comparePos[1] -= 1
                        while(comparePos[1] >= 0):
                            if(grid[comparePos[1]][comparePos[0]] == "#"):
                                if(seenAsteroid == False):
                                    grid[comparePos[1]][comparePos[0]] = "O"
                                    seenAsteroid = True
                                else:
                                    grid[comparePos[1]][comparePos[0]] = "X"
                            comparePos[1] -= 1
                else:
                    top = slope[0]
                    bottom = slope[1]
                    comparePos[1] -= top
                    comparePos[0] -= bottom
                    while(comparePos[0] < len(grid[0]) and comparePos[0] >= 0 and comparePos[1] < len(grid) and comparePos[1] >= 0):
                        if(grid[comparePos[1]][comparePos[0]] == "#"):
                            if(seenAsteroid == False):
                                grid[comparePos[1]][comparePos[0]] = "O"
                                seenAsteroid = True
                            else:
                                grid[comparePos[1]][comparePos[0]] = "X"
                        comparePos[1] -= top
                        comparePos[0] -= bottom
            if(testCase[0] < len(grid) - 1):
                testCase[0] += 1
            else:
                testCase[0] = 0
                testCase[1] += 1
        sum = 0
        for element in grid:
            sum += element.count("O")
        print(sum)
    break
testCase = [0, 0]
asteroids = []
while(testCase[1] < len(grid)):
    if(grid[testCase[1]][testCase[0]] == "O"):
        asteroids.append([math.pi - (math.atan2((testCase[0] - 22), (testCase[1] - 19))), testCase[0], testCase[1]])
    if(testCase[0] < len(grid) - 1):
        testCase[0] += 1
    else:
        testCase[0] = 0
        testCase[1] += 1
for element in asteroids:
    element[0] = element[0] * 180 / math.pi
    if(element[0] < 0):
        element[0] += 360
print(sorted(asteroids)[199])
