import sys
import heapq

N, M, S, E = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost, time = list(map(int, sys.stdin.readline().split()))
    graph[start].append((end, cost, time))
    graph[end].append((start, cost, time))


def isNotEfficient(arr, cost, time):
    return any([(i[0] <= cost) & (i[1] <= time) for i in arr])


visited = [0] * (N + 1)
cost_arr = [[] for _ in range(N + 1)]
heap = []
heapq.heappush(heap, (0, 0, S))
while heap:
    cost, time, node = heapq.heappop(heap)
    if isNotEfficient(cost_arr[node], cost, time) == False:
        cost_arr[node].append((cost, time))
        visited[node] = 1
        for line in graph[node]:
            heapq.heappush(heap, (cost + line[1], time + line[2], line[0]))

print(len(cost_arr[E]))
