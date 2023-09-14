import sys
import math

min, max = list(map(int, sys.stdin.readline().split()))
array = [True for i in range(max - min + 1)]
for i in range(2, int((math.sqrt(max))) + 1):
    print(i)
    j = i * i
    k = min // j if min % j == 0 else (min // j) + 1
    while j * k in range(min, max + 1):
        array[j * k - min] = False
        k += 1
print(array.count(True))
