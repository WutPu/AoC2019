import sys
import math

allData = sys.stdin.read().split('\n')
n = 0
sum = 0

while(n < len(allData)):
    base = (math.floor(int(allData[n]) / 3) - 2)
    sum += base
    while(base > 0):
        base = (math.floor(base / 3) - 2)
        if(base < 0):
            break
        sum += base
    n += 1
print(sum)