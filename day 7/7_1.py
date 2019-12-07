import sys
import itertools
import copy

allData1 = open("7.in").read().split(",")
allData1 = [ int(x) for x in allData1 ]
allData2 = allData1.copy()
allData3 = allData1.copy()
allData4 = allData1.copy()
allData5 = allData1.copy()
datas = []
datas.append(allData1)
datas.append(allData2)
datas.append(allData3)
datas.append(allData4)
datas.append(allData5)

def computer(phase, pointer, nice):
    global outputs
    global datas
    current = 1
    while(True):
        instruction = list(str(datas[nice][pointer]))
        instruction.insert(0, "0")
        instruction.insert(0, "0")
        instruction.insert(0, "0")
        opcode = int(''.join(instruction[-2:]))
        instruction = [ int(x) for x in instruction]
        if(opcode == 99):
            return "complete"
            break
        elif(opcode == 3):
            if(current == 1):
                datas[nice][int(datas[nice][pointer + 1])] = int(phase)
                current = 2
            elif(current == 2):
                return pointer
                break
            pointer += 2
        elif(opcode == 4):
            if(instruction[-3] == 1):
                #immediate mode
                outputs[nice] = str(int(datas[nice][pointer + 1]))
            elif(instruction[-3] == 0):
                #position mode
                outputs[nice] = str(datas[nice][int(datas[nice][pointer + 1])])
            pointer += 2
        elif(opcode == 2):
            value = 0
            if(instruction[-3] == 1):
                if(instruction[-4] == 1):
                    value = int(datas[nice][pointer + 1]) * int(datas[nice][pointer + 2])
                elif(instruction[-4] == 0):
                    value = int(datas[nice][pointer + 1]) * int(datas[nice][int(datas[nice][pointer + 2])])
            elif(instruction[-3] == 0):
                if(instruction[-4] == 1):
                    value = int(datas[nice][int(datas[nice][pointer + 1])]) * int(datas[nice][pointer + 2])
                elif(instruction[-4] == 0):
                    value = int(datas[nice][int(datas[nice][pointer + 1])]) * int(datas[nice][int(datas[nice][pointer + 2])])
            datas[nice][int(datas[nice][pointer + 3])] = value
            pointer += 4
        elif(opcode == 1):
            value = 0
            if(instruction[-3] == 1):
                if(instruction[-4] == 1):
                    value = int(datas[nice][pointer + 1]) + int(datas[nice][pointer + 2])
                elif(instruction[-4] == 0):
                    value = int(datas[nice][pointer + 1]) + int(datas[nice][int(datas[nice][pointer + 2])])
            elif(instruction[-3] == 0):
                if(instruction[-4] == 1):
                    value = int(datas[nice][int(datas[nice][pointer + 1])]) + int(datas[nice][pointer + 2])
                elif(instruction[-4] == 0):
                    value = int(datas[nice][int(datas[nice][pointer + 1])]) + int(datas[nice][int(datas[nice][pointer + 2])])
            datas[nice][int(datas[nice][pointer + 3])] = value
            pointer += 4
        elif(opcode == 5):
            if(instruction[-3] == 1):
                if(int(datas[nice][pointer + 1]) != 0):
                    if(instruction[-4] == 0):
                        pointer = int(datas[nice][int(datas[nice][pointer + 2])])
                    elif(instruction[-4] == 1):
                        pointer = int(datas[nice][pointer + 2])
                else:
                    pointer += 3
            elif(instruction[-3] == 0):
                if(int(datas[nice][int(datas[nice][pointer + 1])]) != 0):
                    if(instruction[-4] == 0):
                        pointer = int(datas[nice][int(datas[nice][pointer + 2])])
                    elif(instruction[-4] == 1):
                        pointer = int(datas[nice][pointer + 2])
                else:
                    pointer += 3
        elif(opcode == 6):
            if(instruction[-3] == 1):
                if(int(datas[nice][pointer + 1]) == 0):
                    if(instruction[-4] == 0):
                        pointer = int(datas[nice][int(datas[nice][pointer + 2])])
                    elif(instruction[-4] == 1):
                        pointer = int(datas[nice][pointer + 2])
                else:
                    pointer += 3
            elif(instruction[-3] == 0):
                if(int(datas[nice][int(datas[nice][pointer + 1])]) == 0):
                    if(instruction[-4] == 0):
                        pointer = int(datas[nice][int(datas[nice][pointer + 2])])
                    elif(instruction[-4] == 1):
                        pointer = int(datas[nice][pointer + 2])
                else:
                    pointer += 3
        elif(opcode == 7):
            value1 = 0
            value2 = 0
            if(instruction[-3] == 1):
                value1 = int(datas[nice][pointer + 1])
            elif(instruction[-3] == 0):
                value1 = int(datas[nice][int(datas[nice][pointer + 1])])
            if(instruction[-4] == 1):
                value2 = int(datas[nice][pointer + 2])
            elif(instruction[-4] == 0):
                value2 = int(datas[nice][int(datas[nice][pointer + 2])])
            if(value1 < value2):
                datas[nice][int(datas[nice][pointer + 3])] = 1
            else:
                datas[nice][int(datas[nice][pointer + 3])] = 0
            pointer += 4
        elif(opcode == 8):
            value1 = 0
            value2 = 0
            if(instruction[-3] == 1):
                value1 = int(datas[nice][pointer + 1])
            elif(instruction[-3] == 0):
                value1 = int(datas[nice][int(datas[nice][pointer + 1])])
            if(instruction[-4] == 1):
                value2 = int(datas[nice][pointer + 2])
            elif(instruction[-4] == 0):
                value2 = int(datas[nice][int(datas[nice][pointer + 2])])
            if(value1 == value2):
                datas[nice][int(datas[nice][pointer + 3])] = 1
            else:
                datas[nice][int(datas[nice][pointer + 3])] = 0
            pointer += 4

bruteForce = list(itertools.permutations(range(5, 10)))
print(bruteForce)
best = 0
for element in bruteForce:
    print(element)
    pointers = [0,0,0,0,0]
    outputs = [0,0,0,0,0]
    pointers[0] = computer(element[0], pointers[0], 0)
    pointers[1] = computer(element[1], pointers[1], 1)
    pointers[2] = computer(element[2], pointers[2], 2)
    pointers[3] = computer(element[3], pointers[3], 3)
    pointers[4] = computer(element[4], pointers[4], 4)
    pointers[0] = computer(0, pointers[0], 0)
    currentCycle = 1
    while(pointers[4] != "complete"):
        print(pointers)
        print(outputs)
        if(currentCycle == 0):
            pointers[0] = computer(outputs[4], pointers[0], 0)
            currentCycle += 1
        elif(currentCycle == 1):
            pointers[1] = computer(outputs[0], pointers[1], 1)
            currentCycle += 1
        elif(currentCycle == 2):
            pointers[2] = computer(outputs[1], pointers[2], 2)
            currentCycle += 1
        elif(currentCycle == 3):
            pointers[3] = computer(outputs[2], pointers[3], 3)
            currentCycle += 1
        elif(currentCycle == 4):
            pointers[4] = computer(outputs[3], pointers[4], 4)
            currentCycle = 0
    if(int(outputs[4]) > best):
        best = int(outputs[4])
print(best)
