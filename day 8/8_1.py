import sys

allData = open("8.in").read()
n = 150

allData = [allData[i:i+n] for i in range(0, len(allData), n)]
allData = [str(x) for x in allData]

best = 9999999999999999
index = -1
for element in allData:
    numberOfZeros = element.count('0')
    if(numberOfZeros < best):
        best = numberOfZeros
        index = allData.index(element)

case = allData[index]
ones = case.count('1')
twos = case.count('2')
print(ones * twos)
