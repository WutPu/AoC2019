import sys
import math

allData = sys.stdin.read().split('\n')
n = 0
sum = 0

while(n < len(allData)):
    sum += (math.floor(int(allData[n]) / 3) - 2)
    n += 1
print(sum)
