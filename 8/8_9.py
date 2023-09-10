import sys
from collections import deque


def ACMCraft():
    N, K = list(map(int, sys.stdin.readline().split()))
    D = list(map(int, sys.stdin.readline().split()))
    graph = {key: [] for key in range(N)}
    graph_rev = {key: [] for key in range(N)}
    vertex = [0] * N
    result = [0] * N
    for _ in range(K):
        X, Y = sys.stdin.readline().split()
        graph[int(X) - 1].append(int(Y) - 1)
        graph_rev[int(Y) - 1].append(int(X) - 1)
        vertex[int(Y) - 1] = vertex[int(Y) - 1] + 1
    W = int(sys.stdin.readline())

    que = deque()
    for i in range(N):
        if vertex[i] == 0:
            que.append(i)

    while len(que) != 0:
        node = que.popleft()
        for next_node in graph[node]:
            vertex[next_node] = vertex[next_node] - 1
            if vertex[next_node] == 0:
                que.append(next_node)

        if len(graph_rev[node]) == 0:
            result[node] = D[node]
        else:
            result[node] = max([result[i] for i in graph_rev[node]]) + D[node]

    print(result[int(W) - 1])


T = int(sys.stdin.readline())

for _ in range(T):
    ACMCraft()
