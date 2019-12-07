import sys
allData = sys.stdin.read().split(",")
backup = allData[:]
print(backup)
pointer = 0
noun = 0
verb = 0
while(True):
    print(str(noun) + " " + str(verb))
    if(int(allData[pointer]) == 1):
        allData[int(allData[pointer + 3])] = int(allData[int(allData[pointer + 2])]) + int(allData[int(allData[pointer + 1])]) 
    elif(int(allData[pointer]) == 2): 
        allData[int(allData[pointer + 3])] = int(allData[int(allData[pointer + 2])]) * int(allData[int(allData[pointer + 1])])
    elif(int(allData[pointer]) == 99):
        if(int(allData[0]) == 19690720):
            print(100 * int(allData[1]) + int(allData[2]))
            break
        else:
            allData = backup[:]
            if(noun == 99):
                verb += 1
                noun = 0
            else:
                noun += 1
            allData[1] = noun
            allData[2] = verb
            print(allData)
            pointer = -4
    pointer += 4
