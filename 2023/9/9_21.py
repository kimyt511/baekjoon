# 1115 순열
import sys
from collections import deque

P = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

visited = [0] * P
answer = 0
while sum(visited) != P:
    curr = visited.index(0)
    while visited[curr] == 0:
        visited[curr] = 1
        curr = arr[curr]
    answer += 1

if answer == 1:
    print(0)
else:
    print(answer)
