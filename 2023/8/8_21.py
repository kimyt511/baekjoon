import sys
import heapq

N, M, X = list(map(int, sys.stdin.readline().split()))
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = list(map(int, sys.stdin.readline().split()))
    roads[start].append((end, time))


def dijkstra(start):
    cost = [sys.maxsize] * (N + 1)
    cost[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    node = [0] * (N + 1)
    while len(heap) != 0:
        time, curr = heapq.heappop(heap)
        node[curr] = 1
        for road in roads[curr]:
            # print(curr, time, road[0], road[1])
            if cost[road[0]] > time + road[1]:
                cost[road[0]] = time + road[1]
                # print(cost[road[0]])
            if node[road[0]] == 0:
                heapq.heappush(heap, (time + road[1], road[0]))
    return cost


forward = [dijkstra(i)[X] for i in range(N + 1)]
backward = dijkstra(X)
print(max([forward[i] + backward[i] for i in range(1, N + 1)]))
