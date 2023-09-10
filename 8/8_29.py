import sys
import heapq

N, M, K = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    graph[start].append((end, cost))
    graph[end].append((start, cost))

visited = [[0] * (K + 1) for _ in range(N + 1)]
cost_arr = [[sys.maxsize] * (K + 1) for _ in range(N + 1)]
heap = []
heapq.heappush(heap, (0, 1, 0))
while heap:
    cost, node, take_out = heapq.heappop(heap)
    if visited[node][take_out] == 0:
        cost_arr[node][take_out] = min(cost_arr[node][take_out], cost)
        visited[node][take_out] = 1
        for line in graph[node]:
            if visited[line[0]][take_out] == 0:
                heapq.heappush(heap, (cost + line[1], line[0], take_out))
            if take_out < K:
                if visited[line[0]][take_out + 1] == 0:
                    heapq.heappush(heap, (cost, line[0], take_out + 1))

print(min(cost_arr[N]))
