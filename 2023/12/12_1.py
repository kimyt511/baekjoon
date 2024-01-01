# 1761 정점들의 거리
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    graph[start - 1].append((end - 1, cost))
    graph[end - 1].append((start - 1, cost))

distance = [0] * N  # 1번 노드를 root 노드로 정한 뒤, 각 노드까지의 거리를 기록
visited = [0] * N
visited[0] = 1
depth = [0] * N  # 각 node가 root 노드인 1번 노드와의 depth 차를 기록
parent = [0] * N  # 각 node의 parent node를 기록
deq = deque()
for c in graph[0]:
    deq.appendleft((c[0], c[1], 0, 1))
while deq:
    curr, dis, p, d = deq.pop()
    if visited[curr] == 0:
        visited[curr] = 1
        distance[curr] = dis
        parent[curr] = p
        depth[curr] = d
        for c in graph[curr]:
            if visited[c[0]] == 0:
                deq.appendleft((c[0], dis + c[1], curr, d + 1))


def get_both_parent(a, b):  # 최소 공통 조상을 찾는다. 이때에 먼저 depth를 맞춘 뒤에 같은 횟수만큼 거슬러 올라가는 방식을 이용
    if depth[a] > depth[b]:
        for _ in range(depth[a] - depth[b]):
            a = parent[a]
    elif depth[a] < depth[b]:
        for _ in range(depth[b] - depth[a]):
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a


M = int(sys.stdin.readline())
for _ in range(M):  # root로부터 start와 end까지의 거리의 합에서 공통조상까지의 거리를 두번 뺴 주어 총 거리를 구함
    start, end = list(map(int, sys.stdin.readline().split()))
    ans = (
        distance[start - 1]
        + distance[end - 1]
        - 2 * distance[get_both_parent(start - 1, end - 1)]
    )
    print(ans)
