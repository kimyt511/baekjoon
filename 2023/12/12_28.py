# 1176 섞기

import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

graph = [[] for _ in range(N)]  # node와 node를 연결하는 graph 형성
for i in range(N):
    for j in range(N):
        if i != j:
            if abs(arr[i] - arr[j]) > K:
                graph[i].append(j)
dp = [
    [0] * (1 << N) for _ in range(N)
]  # 마지막으로 방문한 node와 지금까지 visit 한 node에 대한 bitmask에 가능한 경우의 수

deq = deque()
for i in range(N):
    deq.append((i, (1 << i)))
    dp[i][1 << i] += 1

while deq:
    curr, bitmask = deq.popleft()
    for c in graph[curr]:
        if bitmask & (1 << c):
            continue
        if dp[c][bitmask | (1 << c)] == 0:  # 아직 계산되지 않은 node와 bitmask의 경우 queue에 추가
            deq.append((c, bitmask | (1 << c)))
        dp[c][bitmask | (1 << c)] += dp[curr][
            bitmask
        ]  # 이전 node까지 도달할 수 있었던 경우의 수를, 다음 node에 도달할 때에 더함

ans = 0
for i in range(N):  # 가능한 모든 배열 경우의 수의 합
    ans += dp[i][(1 << N) - 1]
print(ans)
