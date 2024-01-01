# 1131 숫자
import sys

A, B, K = list(map(int, sys.stdin.readline().split()))
multiple_arr = [i**K for i in range(0, 10)]


def Sk(num):
    sum = 0
    for i in str(num):
        sum += multiple_arr[int(i)]
    return sum


dic = {}


def getMinimum(num):
    if num in dic:
        return dic[num]
    curr = num
    arr = []
    while True:
        if curr in arr:
            idx = arr.index(curr)
            break
        if curr in dic:
            arr.append(dic[curr])
            idx = len(arr)
            break
        arr.append(curr)
        curr = Sk(curr)
    for i in range(len(arr)):
        if i >= idx:
            dic[arr[i]] = min(arr[idx:])
        else:
            dic[arr[i]] = min(arr[i:])
    return dic[num]


sum = 0
for i in range(A, B + 1):
    sum += getMinimum(i)
print(sum)
