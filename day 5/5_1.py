import sys

allData = open("5.in").read().split(",")
allData = [ int(x) for x in allData ]
print(allData)
print(allData[238])
inputs = 5
pointer = 0

while(True):
    instruction = list(str(allData[pointer]))
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    instruction.insert(0, "0")
    opcode = int(''.join(instruction[-2:]))
    print(str(pointer) + ": " + str(allData[pointer]))
    instruction = [ int(x) for x in instruction ]
    if(opcode == 99):
        break
    elif(opcode == 3):
        allData[int(allData[pointer + 1])] = int(inputs)
        pointer += 2
    elif(opcode == 4):
        if(instruction[-3] == 1):
            #immediate mode
            print(int(allData[pointer + 1]))
        elif(instruction[-3] == 0):
            #position mode
            print(allData[int(allData[pointer + 1])])
        pointer += 2
    elif(opcode == 2):
        value = 0
        if(instruction[-3] == 1):
            if(instruction[-4] == 1):
                value = int(allData[pointer + 1]) * int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[pointer + 1]) * int(allData[int(allData[pointer + 2])])
        elif(instruction[-3] == 0):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1])]) * int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1])]) * int(allData[int(allData[pointer + 2])])    
        allData[int(allData[pointer + 3])] = value
        pointer += 4
    elif(opcode == 1):
        value = 0
        if(instruction[-3] == 1):
            if(instruction[-4] == 1):
                value = int(allData[pointer + 1]) + int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[pointer + 1]) + int(allData[int(allData[pointer + 2])])
        elif(instruction[-3] == 0):
            if(instruction[-4] == 1):
                value = int(allData[int(allData[pointer + 1])]) + int(allData[pointer + 2])
            elif(instruction[-4] == 0):
                value = int(allData[int(allData[pointer + 1])]) + int(allData[int(allData[pointer + 2])])
        allData[int(allData[pointer + 3])] = value
        pointer += 4
    elif(opcode == 5):
        print(instruction)
        if(instruction[-3] == 1):
            if(int(allData[pointer + 1]) != 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    print(allData)
                    pointer = int(allData[pointer + 2])
            else:
                pointer += 3
        elif(instruction[-3] == 0):
            if(int(allData[int(allData[pointer + 1])]) != 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
            else:
                pointer += 3
    elif(opcode == 6):
        if(instruction[-3] == 1):
            if(int(allData[pointer + 1]) == 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
            else:
                pointer += 3
        elif(instruction[-3] == 0):
            if(int(allData[int(allData[pointer + 1])]) == 0):
                if(instruction[-4] == 0):
                    pointer = int(allData[int(allData[pointer + 2])])
                elif(instruction[-4] == 1):
                    pointer = int(allData[pointer + 2])
            else:
                pointer += 3
    elif(opcode == 7):
        value1 = 0
        value2 = 0
        if(instruction[-3] == 1):
            value1 = int(allData[pointer + 1])    
        elif(instruction[-3] == 0):
            value1 = int(allData[int(allData[pointer + 1])])
        if(instruction[-4] == 1):
            value2 = int(allData[pointer + 2])    
        elif(instruction[-4] == 0):
            value2 = int(allData[int(allData[pointer + 2])])
        if(value1 < value2):
            allData[int(allData[pointer + 3])] = 1
        else:
            allData[int(allData[pointer + 3])] = 0
        pointer += 4
    elif(opcode == 8):
        value1 = 0
        value2 = 0
        if(instruction[-3] == 1):
            value1 = int(allData[pointer + 1])    
        elif(instruction[-3] == 0):
            value1 = int(allData[int(allData[pointer + 1])])
        if(instruction[-4] == 1):
            value2 = int(allData[pointer + 2])    
        elif(instruction[-4] == 0):
            value2 = int(allData[int(allData[pointer + 2])])
        if(value1 == value2):
            allData[int(allData[pointer + 3])] = 1
        else:
            allData[int(allData[pointer + 3])] = 0
        pointer += 4
