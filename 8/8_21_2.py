import sys
import heapq
import math

# sys.stdin=open("input.txt")

N, X, T = map(int, sys.stdin.readline().split())


def dijk(start, end, gph):
    dist = [math.inf for _ in range(N + 2)]
    edges = []

    dist[start] = 0
    heapq.heappush(edges, (dist[start], start))

    while edges:
        cost, pos = heapq.heappop(edges)
        for p, c in gph[pos]:
            c += cost
            if dist[p] > c:
                dist[p] = c
                print(p, c)
                heapq.heappush(edges, (c, p))

    return dist[end]


gph = [[] for _ in range(N + 2)]
gph_back = [[] for _ in range(N + 2)]
while X:
    X -= 1
    a, b, c = map(int, sys.stdin.readline().split())
    gph[a].append((b, c))
    gph_back[b].append((a, c))

"""m = 0
for idx in range(N):
    m = max(m, dijk(idx + 1, T, gph) + dijk(T, idx + 1, gph))
print(m)"""
print(dijk(7, T, gph))
