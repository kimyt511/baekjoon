import sys
import math
from collections import deque

N = int(sys.stdin.readline())
ratio = [0] * N
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, p, q = list(map(int, sys.stdin.readline().split()))
    graph[a].append((a, b, p, q))
    graph[b].append((b, a, q, p))

start = list(filter(lambda x: len(x) == 1, graph))[0][0]
deq = deque()
deq.append(start)
while len(deq) != 0:
    a, b, p, q = deq.pop()
    if (ratio[a] == 0) & (ratio[b] == 0):
        ratio[a] = p
        ratio[b] = q
    else:
        ratio = [x * p for x in ratio]
        ratio[b] = ratio[a] / p * q
    for i in graph[b]:
        if (i[1] != a) & (ratio[i[1]] == 0):
            deq.append(i)

print(" ".join([str(int(i / math.gcd(*list(map(int, ratio))))) for i in ratio]))
