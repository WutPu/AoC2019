import numpy as np
import sys
from scipy.sparse import coo_matrix
np.set_printoptions(threshold=sys.maxsize)

directions = sys.stdin.read().split("\n")
wireOne = directions[0].split(",")
wireTwo = directions[1].split(",")

#grid = np.zeros((14000, 14000))
grid = coo_matrix((25000, 25000), dtype=np.int8).toarray()
grid[12500][12500] = 99

#wire one
pointerX = 12500
pointerY = 12500
for x in range(len(wireOne)):
    currentMove = wireOne[x]
    print(str(pointerX) + " " + str(pointerY) + " " + str(currentMove))
    direction = currentMove[0]
    number = int(currentMove[1:len(currentMove) + 1])
    step = 0
    if(direction == "U"):
        while(step < number):
            step += 1
            pointerX -= 1
            grid[pointerX][pointerY] = 1
    elif(direction == "D"):
        while(step < number):
            step += 1
            pointerX += 1
            grid[pointerX][pointerY] = 1
    elif(direction == "L"):
        while(step < number):
            step += 1
            pointerY -= 1
            grid[pointerX][pointerY] = 1
    elif(direction == "R"):
        while(step < number):
            step += 1
            pointerY += 1
            grid[pointerX][pointerY] = 1
    else:
        print("nice job screwing up the input data idiot")

#wire two
print("computing wire two")
pointerX = 12500
pointerY = 12500
for x in range(len(wireTwo)):
    currentMove = wireTwo[x]
    print(str(pointerX) + " " + str(pointerY) + " " + str(currentMove))
    direction = currentMove[0]
    number = int(currentMove[1:len(currentMove) + 1])
    step = 0
    if(direction == "U"):
        while(step < number):
            step += 1
            pointerX -= 1
            if(grid[pointerX][pointerY] == 1):
                grid[pointerX][pointerY] = 2
            else:
                grid[pointerX][pointerY] = 3
    elif(direction == "D"):
        while(step < number):
            step += 1
            pointerX += 1
            if(grid[pointerX][pointerY] == 1):
                grid[pointerX][pointerY] = 2
            else:
                grid[pointerX][pointerY] = 3
    elif(direction == "L"):
        while(step < number):
            step += 1
            pointerY -= 1
            if(grid[pointerX][pointerY] == 1):
                grid[pointerX][pointerY] = 2
            else:
                grid[pointerX][pointerY] = 3
    elif(direction == "R"):
        while(step < number):
            step += 1
            pointerY += 1
            if(grid[pointerX][pointerY] == 1):
                grid[pointerX][pointerY] = 2
            else:
                grid[pointerX][pointerY] = 3
    else:
        print("nice job")
intersections = np.where(grid == 2)
#check = np.where(grid == 3)
listOfCoordinates= list(zip(intersections[0], intersections[1]))
#listCheck = list(zip(check[0], check[1]))
print(listOfCoordinates)
#print(listCheck)

#find steps
pointerX = 12500
pointerY = 12500
i = []
totalsteps = 0
for x in range(len(wireOne)):
    currentMove = wireOne[x]
    print(str(pointerX) + " " + str(pointerY) + " " + str(currentMove))
    direction = currentMove[0]
    number = int(currentMove[1:len(currentMove) + 1])
    step = 0
    if(direction == "U"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerX -= 1
            if(grid[pointerX][pointerY] == 2):
                place = []
                place.append(pointerX)
                place.append(pointerY)
                place.append(totalsteps)
                i.append(place)
    elif(direction == "D"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerX += 1
            if(grid[pointerX][pointerY] == 2):
                place = []
                place.append(pointerX)
                place.append(pointerY)
                place.append(totalsteps)
                i.append(place)
    elif(direction == "L"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerY -= 1
            if(grid[pointerX][pointerY] == 2):
                place = []
                place.append(pointerX)
                place.append(pointerY)
                place.append(totalsteps)
                i.append(place)
    elif(direction == "R"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerY += 1
            if(grid[pointerX][pointerY] == 2):
                place = []
                place.append(pointerX)
                place.append(pointerY)
                place.append(totalsteps)
                i.append(place)
    else:
        print("nice job")
print(i)
totals = []
pointerX = 12500
pointerY = 12500
totalsteps = 0
for x in range(len(wireTwo)):
    currentMove = wireTwo[x]
    direction = currentMove[0]
    number = int(currentMove[1:len(currentMove) + 1])
    step = 0
    if(direction == "U"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerX -= 1
            if(grid[pointerX][pointerY] == 2):
                for l in range(len(i)):
                    test = i[l]
                    if(test[0] == pointerX and test[1] == pointerY):
                        best = test[2] + totalsteps
                        totals.append(best)
                        del i[l]
                        break
    elif(direction == "D"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerX += 1
            if(grid[pointerX][pointerY] == 2):
                for l in range(len(i)):
                    test = i[l]
                    if(test[0] == pointerX and test[1] == pointerY):
                        best = test[2] + totalsteps
                        totals.append(best)
                        del i[l]
                        break
    elif(direction == "L"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerY -= 1
            if(grid[pointerX][pointerY] == 2):
                for l in range(len(i)):
                    test = i[l]
                    if(test[0] == pointerX and test[1] == pointerY):
                        best = test[2] + totalsteps
                        totals.append(best)
                        del i[l]
                        break
    elif(direction == "R"):
        while(step < number):
            step += 1
            totalsteps += 1
            pointerY += 1
            if(grid[pointerX][pointerY] == 2):
                for l in range(len(i)):
                    test = i[l]
                    if(test[0] == pointerX and test[1] == pointerY):
                        best = test[2] + totalsteps
                        totals.append(best)
                        del i[l]
                        break

print(sorted(totals))
