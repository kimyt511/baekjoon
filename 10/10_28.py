# 1219 오민식의 고민
import sys
from collections import deque

N, start, end, M = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N)]

for _ in range(M):
    s, e, c = list(map(int, sys.stdin.readline().split()))
    graph[s].append((e, c))

money_arr = list(map(int, sys.stdin.readline().split()))


def check_possible(n):  # n번째 노드에서 end 노드까지 도달이 가능한지 확인
    deq = deque([n])
    visited = [0] * N
    while deq:
        node = deq.pop()
        if node == end:
            return True
        if visited[node] == 0:
            visited[node] = 1
            for c in graph[node]:
                deq.append(c[0])
    return False


reachable_arr = [check_possible(i) for i in range(N)]
if reachable_arr[start] == False:  # start에서 end로 도달이 불가능하다면 gg를 출력
    print("gg")
    exit()
cost_arr = [sys.maxsize] * N  # bellman-ford 알고리즘
cost_arr[start] = -money_arr[start]
for _ in range(N):
    deq = deque([start])
    visited = [0] * N
    while deq:
        node = deq.pop()
        if visited[node] == 0:
            visited[node] = 1
            for c in graph[node]:
                cost_arr[c[0]] = min(
                    cost_arr[c[0]], cost_arr[node] + c[1] - money_arr[c[0]]
                )
                deq.append(c[0])

deq = deque([start])  # 음의 사이클이 있는지 확인
visited = [0] * N
while deq:
    node = deq.pop()
    if visited[node] == 0:
        visited[node] = 1
        for c in graph[node]:
            if cost_arr[c[0]] > cost_arr[node] + c[1] - money_arr[c[0]]:
                if reachable_arr[c[0]]:  # 해당 사이클에서 end로 도달이 가능하다면 Gee 출력
                    print("Gee")
                    exit()
            deq.append(c[0])

print(-cost_arr[end])
