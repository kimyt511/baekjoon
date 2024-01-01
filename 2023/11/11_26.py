# 1635 1 또는 -1
import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(N):  # 1과 -1이 구분된 N개의 수열 생성
    _arr = [-1] * N
    for j in range(i, N):
        _arr[j] = 1
    arr.append(_arr)

for _ in range(M):
    curr = list(map(int, sys.stdin.readline().split()))
    Flag = False
    for a in arr:  # arr 내에서 적절한 수열을 찾는다
        if Flag:
            break
        sum = 0
        for i in range(N):
            sum += a[i] * curr[i]
        if sum == 0:
            print(*a)
            Flag = True
