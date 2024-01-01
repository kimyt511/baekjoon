# 2188 축사 배정
import sys

N, M = list(map(int, sys.stdin.readline().split()))
graph = []
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr[1:])

cage_arr = [-1] * (M + 1)
visited = [0] * (M + 1)


def matching(cow):
    for i in graph[cow]:
        if visited[i] == 0:
            visited[i] = 1
            if cage_arr[i] == -1:
                cage_arr[i] = cow
                return True
            if matching(cage_arr[i]):
                cage_arr[i] = cow
                return True
    return False


ans = 0
for i in range(N):
    visited = [0] * (M + 1)
    if matching(i):
        ans += 1
print(ans)
