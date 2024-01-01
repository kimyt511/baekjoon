# 1045 도로
# 크루스칼 알고리즘을 통해 MST 생성
import sys

N, M = list(map(int, sys.stdin.readline().split()))
graph = []
for i in range(N):
    line = sys.stdin.readline()
    for j in range(len(line)):
        if (line[j] == "Y") & ((j, i) not in graph):
            graph.append((i, j))
if len(graph) < M:
    print(-1)
    exit()
graph.sort()
parents = list(range(N))
route = []
edge_num = 0


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


for v in graph:
    if find(parents, v[0]) != find(parents, v[1]):
        union(parents, v[0], v[1])
        route.append(v)
        edge_num += 1

if edge_num != N - 1:
    print(-1)
    exit()
else:
    for v in graph:
        if edge_num == M:
            break
        if v not in route:
            route.append(v)
            edge_num += 1
    node = [0] * N
    for r in route:
        node[r[0]] += 1
        node[r[1]] += 1
    print(" ".join(list(map(str, node))))
