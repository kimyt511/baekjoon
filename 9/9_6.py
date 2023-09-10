import sys
import math

x, b = list(map(int, sys.stdin.readline().split()))
minus = False
arr = []
if (x > 0) & (b > 0):
    while x != 0:
        arr.append(x % b)
        x = int((x - x % b) / b)
elif (x < 0) & (b > 0):
    while x != 0:
        arr.append(abs(x) % b)
        x = int((x + abs(x) % b) / b)
    minus = True
elif b < 0:
    c = -1
    while x != 0:
        if c > 0:
            next = x % b
            if next < 0:
                next = next - b
        else:
            next = x % abs(b)
        arr.append(next)
        x = int((x - next) / b)
        c = -c

if len(arr) == 0:
    print(0)
else:
    arr = list(map(str, arr))
    answer = "".join(reversed(arr))
    if minus:
        print("-" + answer)
    else:
        print(answer)
