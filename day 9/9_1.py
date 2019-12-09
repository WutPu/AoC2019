import sys

allData = open("9.in").read().split(",")
allData = [int(x) for x in allData]
inputs = 2
pointer = 0
relativeBase = 0

for x in range(1000):
    allData.append(0)

while(True):
    instruction = list(str(allData[pointer]))
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    opcode = int(''.join(instruction[-2:]))
    #print(str(pointer) + ": " + str(allData[pointer]) + ":" + str(relativeBase))
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
            print(allData[pointer + 1])
        elif(instruction[-3] == 0):
            #position mode
            print(allData[allData[pointer + 1]])
        elif(instruction[-3] == 2):
            print(allData[allData[pointer + 1] + relativeBase])
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
