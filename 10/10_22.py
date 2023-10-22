# 1090 체커

import sys

N = int(sys.stdin.readline())
checker_arr = []
for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    checker_arr.append((x, y))

answer = [sys.maxsize] * N
for i in range(N):
    for j in range(N):
        arr = []
        for k in range(N):
            distance = abs(checker_arr[k][0] - checker_arr[i][0]) + abs(
                checker_arr[k][1] - checker_arr[j][1]
            )
            arr.append(distance)
        arr.sort()
        temp = 0
        for k in range(N):
            temp += arr[k]
            answer[k] = min(answer[k], temp)

print(*answer)
