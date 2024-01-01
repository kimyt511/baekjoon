# 1178 간선추가
import sys
from collections import deque

V, E = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(V)]
for _ in range(E):  # 주어진 간선으로 그래프 생성
    start, end = list(map(int, sys.stdin.readline().split()))
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)


def get_connected(idx):  # 주어진 node와 연결된 모든 node를 idx로 갖는 값을 1로 표시한 배열을 반환
    visited = [0] * V
    deq = [idx]
    while deq:
        node = deq.pop()
        if visited[node] == 0:
            visited[node] = 1
            for c in graph[node]:
                if visited[c] == 0:
                    deq.append(c)
    return visited


visited = [0] * V
count = 0
group_data = []
while count != V:
    odd_num = 0
    node = visited.index(0)
    arr = get_connected(node)
    for i in range(V):
        if arr[i] == 1:
            if len(graph[i]) % 2 == 1:
                odd_num += 1
            visited[i] = 1
            count += 1
    group_data.append(odd_num)  # 몇 개의 연결된 그룹으로 나뉘는지, 해당 그룹에는 몇 개의 홀수 간선을 갖는 node가 있는지

# 홀수가 존재하는 그룹끼리는 연결될 때에 추가적인 간선이 필요하지 않다.
# 홀수가 존재하지 않는 그룹이 연결될 때에는 추가적인 간선이 하나 필요함.
print(group_data.count(0) + max(0, sum(group_data) // 2 - 1))
