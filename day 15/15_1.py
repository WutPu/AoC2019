import sys
import random
import _pickle as cPickle

allData = [int(x) for x in open("15.in").read().split(",")]
inputs = 1
pointer = 0
relativeBase = 0
grid = []
results = []
for x in range(70):
    element = []
    for x in range(70):
        element.append(" ")
    grid.append(element)
robot = [34, 34]
grid[robot[1]][robot[0]] = "S"
while(True):
    if(len(results) != 0):
        if(results[0] == 0):
            if(inputs == 1):
                grid[robot[1] - 1][robot[0]] = "#"
            elif(inputs == 2):
                grid[robot[1] + 1][robot[0]] = "#"
            elif(inputs == 3):
                grid[robot[1]][robot[0] - 1] = "#"
            elif(inputs == 4):
                grid[robot[1]][robot[0] + 1] = "#"
        elif(results[0] == 1):
            if(inputs == 1):
                robot[1] -= 1
            elif(inputs == 2):
                robot[1] += 1
            elif(inputs == 3):
                robot[0] -= 1
            elif(inputs == 4):
                robot[0] += 1
            grid[robot[1]][robot[0]] = "."
        elif(results[0] == 2):
            if(inputs == 1):
                robot[1] -= 1
            elif(inputs == 2):
                robot[1] += 1
            elif(inputs == 3):
                robot[0] -= 1
            elif(inputs == 4):
                robot[0] += 1
            grid[robot[1]][robot[0]] = "O"
        grid2 = cPickle.loads(cPickle.dumps(grid, -1))
        for element in grid2:
            grid2[robot[1]][robot[0]] = "D"
            print(''.join(element))
        del results[0]
    grid[34][34] = "S"
    instruction = list(str(allData[pointer]))
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    opcode = int(''.join(instruction[-2:]))
    #print(str(pointer) + ": " + str(allData[pointer]) + ":" + str(relativeBase))
    instruction = [ int(x) for x in instruction ]
    if(opcode == 99):
        break
    elif(opcode == 3):
        while(True):
            inputs = random.randint(1, 4)
            if(inputs == 1):
                if(grid[robot[1] - 1][robot[0]] == " "):
                    break
            elif(inputs == 2):
                if(grid[robot[1] + 1][robot[0]] == " "):
                    break
            elif(inputs == 3):
                if(grid[robot[1]][robot[0] - 1] == " "):
                    break
            elif(inputs == 4):
                if(grid[robot[1]][robot[0] + 1] == " "):
                    break
            if(grid[robot[1] - 1][robot[0]] != " " and grid[robot[1] + 1][robot[0]] != " " and grid[robot[1]][robot[0] - 1] != " " and grid[robot[1]][robot[0] + 1] != " "):
                while(True):
                    print("input required:")
                    user = input()
                    if(user.isdigit() == True and int(user) < 5 and int(user) > 0):
                        inputs = int(user)
                        break
                break
        if(instruction[-3] == 0):
            allData[allData[pointer + 1]] = inputs
        elif(instruction[-3] == 2):
            allData[allData[pointer + 1] + relativeBase] = inputs
        pointer += 2
    elif(opcode == 4):
        if(instruction[-3] == 1):
            #immediate mode
            results.append(allData[pointer + 1])
        elif(instruction[-3] == 0):
            #position mode
            results.append(allData[allData[pointer + 1]])
        elif(instruction[-3] == 2):
            results.append(allData[allData[pointer + 1] + relativeBase])
        pointer += 2
    elif(opcode == 2):
        value = 0
        if(instruction[-3] == 1):
            if(instruction[-4] == 1):
                value = int(allData[pointer + 1]) * int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[pointer + 1]) * int(allData[int(allData[pointer + 2])])
            elif(instruction[-4] == 2):
                value = int(allData[pointer + 1]) * int(allData[int(allData[pointer + 2]) + relativeBase])
        elif(instruction[-3] == 0):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1])]) * int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1])]) * int(allData[int(allData[pointer + 2])])
            elif(instruction[-4] == 2):
                value = int(allData[int(allData[pointer + 1])]) * int(allData[int(allData[pointer + 2]) + relativeBase])
        elif(instruction[-3] == 2):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) * int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) * int(allData[int(allData[pointer + 2])])
            elif(instruction[-4] == 2):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) * int(allData[int(allData[pointer + 2]) + relativeBase])
        if(instruction[-5] == 0):
            allData[int(allData[pointer + 3])] = value
        elif(instruction[-5] == 2):
            allData[int(allData[pointer + 3]) + relativeBase] = value
        pointer += 4
    elif(opcode == 1):
        value = 0
        if(instruction[-3] == 1):
            if(instruction[-4] == 1):
                value = int(allData[pointer + 1]) + int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[pointer + 1]) + int(allData[int(allData[pointer + 2])])
            elif(instruction[-4] == 2):
                value = int(allData[pointer + 1]) + int(allData[int(allData[pointer + 2]) + relativeBase])
        elif(instruction[-3] == 0):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1])]) + int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1])]) + int(allData[int(allData[pointer + 2])]) 
            elif(instruction[-4] == 2):
                value = int(allData[int(allData[pointer + 1])]) + int(allData[int(allData[pointer + 2]) + relativeBase])  
        elif(instruction[-3] == 2):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) + int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) + int(allData[int(allData[pointer + 2])]) 
            elif(instruction[-4] == 2):
                value = int(allData[int(allData[pointer + 1]) + relativeBase]) + int(allData[int(allData[pointer + 2]) + relativeBase])  
        if(instruction[-5] == 0):
            allData[int(allData[pointer + 3])] = value
        elif(instruction[-5] == 2):
            allData[int(allData[pointer + 3]) + relativeBase] = value
        pointer += 4
    elif(opcode == 5):
        if(instruction[-3] == 1):
            if(int(allData[pointer + 1]) != 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
        elif(instruction[-3] == 0):
            if(int(allData[int(allData[pointer + 1])]) != 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
        elif(instruction[-3] == 2):
            if(int(allData[int(allData[pointer + 1]) + relativeBase]) != 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
    elif(opcode == 6):
        if(instruction[-3] == 1):
            if(int(allData[pointer + 1]) == 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
        elif(instruction[-3] == 0):
            if(int(allData[int(allData[pointer + 1])]) == 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
        elif(instruction[-3] == 2):
            if(int(allData[int(allData[pointer + 1]) + relativeBase]) == 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
                elif(instruction[-4] == 2):
                    pointer = int(allData[int(allData[pointer + 2]) + relativeBase])
            else:
                pointer += 3
    elif(opcode == 7):
        value1 = 0
        value2 = 0
        if(instruction[-3] == 1):
            value1 = int(allData[pointer + 1])
        elif(instruction[-3] == 0):
            value1 = int(allData[int(allData[pointer + 1])])
        elif(instruction[-3] == 2):
            value1 = int(allData[int(allData[pointer + 1]) + relativeBase])
        if(instruction[-4] == 1):
            value2 = int(allData[pointer + 2])
        elif(instruction[-4] == 0):
            value2 = int(allData[int(allData[pointer + 2])])
        elif(instruction[-4] == 2):
            value2 = int(allData[int(allData[pointer + 2]) + relativeBase])
        if(value1 < value2):
            if(instruction[-5] == 0):
                allData[int(allData[pointer + 3])] = 1
            elif(instruction[-5] == 2):
                allData[int(allData[pointer + 3]) + relativeBase] = 1
        else:
            if(instruction[-5] == 0):
                allData[int(allData[pointer + 3])] = 0
            elif(instruction[-5] == 2):
                allData[int(allData[pointer + 3]) + relativeBase] = 0
        pointer += 4
    elif(opcode == 8):
        value1 = 0
        value2 = 0
        if(instruction[-3] == 1):
            value1 = int(allData[pointer + 1])
        elif(instruction[-3] == 0):
            value1 = int(allData[int(allData[pointer + 1])])
        elif(instruction[-3] == 2):
            value1 = int(allData[int(allData[pointer + 1]) + relativeBase])
        if(instruction[-4] == 1):
            value2 = int(allData[pointer + 2])
        elif(instruction[-4] == 0):
            value2 = int(allData[int(allData[pointer + 2])])
        elif(instruction[-4] == 2):
            value2 = int(allData[int(allData[pointer + 2]) + relativeBase])
        if(value1 == value2):
            if(instruction[-5] == 0):
                allData[int(allData[pointer + 3])] = 1
            elif(instruction[-5] == 2):
                allData[int(allData[pointer + 3]) + relativeBase] = 1
        else:
            if(instruction[-5] == 0):
                allData[int(allData[pointer + 3])] = 0
            elif(instruction[-5] == 2):
                allData[int(allData[pointer + 3]) + relativeBase] = 0
        pointer += 4
    elif(opcode == 9):
        if(instruction[-3] == 0):
            relativeBase += allData[allData[pointer + 1]]
        elif(instruction[-3] == 1):
            relativeBase += allData[pointer + 1]
        elif(instruction[-3] == 2):
            relativeBase += allData[allData[pointer + 1] + relativeBase]
        pointer += 2

for element in grid:
    print(''.join(element))
