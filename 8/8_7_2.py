import sys

C, N = list(map(int, sys.stdin.readline().split()))
arr = [0] * C
citys = []


def getVal(idx):
    if idx < 0:
        return 0
    else:
        return arr[idx]


for i in range(N):
    citys.append(tuple(list(map(int, sys.stdin.readline().split()))))
for i in range(C):
    val = []
    for city in citys:
        val.append(city[0] + getVal(i - city[1]))
    arr[i] = min(val)

print(arr[C - 1])
