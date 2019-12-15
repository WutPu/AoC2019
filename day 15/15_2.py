import sys
import pickle

field = [list(x) for x in open("15grid.in").read().split("\n")]

def checker(grid):
    oxygen = True
    for element in grid:
        if("." in element):
            oxygen = False
    return oxygen

def spread(grid):
    oxygenLocations = []
    y = 0
    while(y < len(grid)):
        x = 0
        while(x < len(grid[y])):
            if(grid[y][x] == "O"):
                oxygenLocations.append([x, y])
            x += 1
        y += 1
    for element in oxygenLocations:
        if(grid[element[1] - 1][element[0]] == "."):
            grid[element[1] - 1][element[0]] = "O"
        if(grid[element[1] + 1][element[0]] == "."):
            grid[element[1] + 1][element[0]] = "O"
        if(grid[element[1]][element[0] - 1] == "."):
            grid[element[1]][element[0] - 1] = "O"
        if(grid[element[1]][element[0] + 1] == "."):
            grid[element[1]][element[0] + 1] = "O"

steps = 0
while(checker(field) != True):
    spread(field)
    steps += 1
    for element in field:
        print(''.join(element))
print(steps)
