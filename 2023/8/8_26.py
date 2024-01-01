import sys
import heapq

V, E = list(map(int, sys.stdin.readline().split()))
start_node = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    graph[start].append((end, cost))

visited = [0] * (V + 1)
cost_arr = [sys.maxsize] * (V + 1)
heap = []
heapq.heappush(heap, (0, start_node))
while heap:
    cost, node = heapq.heappop(heap)
    if visited[node] == 0:
        cost_arr[node] = min(cost_arr[node], cost)
        visited[node] = 1
        for line in graph[node]:
            if visited[line[0]] == 0:
                heapq.heappush(heap, (cost + line[1], line[0]))

for i in range(1, len(cost_arr)):
    if cost_arr[i] == sys.maxsize:
        print("INF")
    else:
        print(cost_arr[i])
