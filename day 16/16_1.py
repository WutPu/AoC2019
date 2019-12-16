import sys
from itertools import repeat

fft = [int(x) for x in list(open("16.in").read())]
pattern = [0, 1, 0, -1]
upperLimit = 100
for x in range(upperLimit):
    counter = 1
    newfft = []
    while(counter <= len(fft)):
        currentPattern = [x for item in pattern[:] for x in repeat(item, counter)]
        currentPattern *= (len(fft) // len(currentPattern)) + 1 
        del currentPattern[0]
        fftCopy = fft[:]
        counter2 = 0
        while(counter2 < len(fftCopy)):
            fftCopy[counter2] = fftCopy[counter2] * currentPattern[counter2]
            counter2 += 1
        newfft.append(int(str(sum(fftCopy))[-1]))
        counter += 1
    fft = newfft[:]
    print("phase: " + str(x + 1) + " " + str(newfft))
