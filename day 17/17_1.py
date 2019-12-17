import sys

allData = [int(x) for x in open("17.in").read().split(",")]
inputs = 0
pointer = 0
relativeBase = 0

for x in range(100000):
    allData.append(0)

results = []
while(True):
    instruction = list(str(allData[pointer]))
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    opcode = int(''.join(instruction[-2:]))
    instruction = [ int(x) for x in instruction ]
    if(opcode == 99):
        break
    elif(opcode == 3):
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
sti = ""
for element in results:
    sti += chr(element)
print(sti)
rid = sti.split("\n")
rid = [list(x) for x in rid]
print([len(rid), len(rid[0])])
del rid[-1]
del rid[-1]

def intersections(grid):
    xs = []
    y = 0
    while(y < len(grid)):
        x = 0
        if(y > 0 and y < len(grid) - 1):
            while(x < len(grid[y])):
                if(x > 0 and x < len(grid[y]) - 1):
                    print("\n" + str([x,y]))
                    print(" " + grid[y - 1][x] + " " + "\n" + grid[y][x - 1] + grid[y][x] + grid[y][x + 1] + "\n" + " " + grid[y + 1][x] + " ")
                    print(len(grid), len(grid[y]))
                    if(grid[y][x] == "#"):
                        if(grid[y - 1][x] == "#" and grid[y + 1][x] == "#" and grid[y][x - 1] == "#" and grid[y][x + 1] == "#"):
                            xs.append([x, y])
                x += 1
        y += 1
    return xs

i = intersections(rid)
sum = 0
for element in i:
    sum += element[0] * element[1]
print(sum)
