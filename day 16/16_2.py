import sys
from itertools import accumulate

fft = [int(x) for x in list(open("16.in").read())] * 10000
half = fft[int(len(fft) / 2) : len(fft) + 1]
offset = int(''.join(str(x) for x in fft[:7])) - int(len(fft) / 2)
upperLimit = 100
for x in range(upperLimit):
    print(x)
    half = [int(str(x)[-1]) for x in list(accumulate((half)[::-1]))[::-1]]
print(half[(offset) : (offset + 8)])
