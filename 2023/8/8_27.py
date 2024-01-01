import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    graph[start].append((end, cost))
    graph[end].append((start, cost))


def dijkstra(start_node):
    visited = [0] * (n + 1)
    cost_arr = [(-1, 0)] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, start_node, 0))
    while heap:
        cost, node, first_visit_node = heapq.heappop(heap)
        if visited[node] == 0:
            cost_arr[node] = (cost, first_visit_node)
            visited[node] = 1
            for line in graph[node]:
                if visited[line[0]] == 0:
                    if first_visit_node == 0:
                        heapq.heappush(heap, (cost + line[1], line[0], line[0]))
                    else:
                        heapq.heappush(
                            heap, (cost + line[1], line[0], first_visit_node)
                        )

    return cost_arr


for i in range(n):
    arr = dijkstra(i + 1)
    arr = ["-" if arr[j][1] == 0 else str(arr[j][1]) for j in range(1, len(arr))]
    print(" ".join(arr))
