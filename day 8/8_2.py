import sys
import re

allData = open("8.in").read()
n = 150

allData = [allData[i:i+n] for i in range(0, len(allData), n)]

#0 is black, 1 is white, 2 is transparent

finalResult = []

counter = 0
while(counter < n):
    for element in allData:
        if(int(element[counter]) == 0):
            finalResult.append('0')
            break
        elif(int(element[counter]) == 1):
            finalResult.append('1')
            break
    counter += 1
clean = ''.join(finalResult)
print(re.sub("(.{25})", "\\1\n", clean, 0, re.DOTALL))
