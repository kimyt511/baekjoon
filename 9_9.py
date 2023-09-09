import sys
import heapq

V = int(sys.stdin.readline())
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    vertex_arr = list(map(int, sys.stdin.readline().split()))
    for i in range(int((len(vertex_arr) - 2) / 2)):
        tree[vertex_arr[0]].append((vertex_arr[2 * i + 1], vertex_arr[2 * i + 2]))


def dijkstra(node):
    heap = []
    heapq.heappush(heap, (0, node))
    cost_arr = [sys.maxsize] * (V + 1)
    visited = [0] * (V + 1)
    while heap:
        cost, curr = heapq.heappop(heap)
        if visited[curr] == 0:
            visited[curr] = 1
            cost_arr[curr] = min(cost_arr[curr], cost)
            for i in tree[curr]:
                if visited[i[0]] == 0:
                    heapq.heappush(heap, (cost + i[1], i[0]))
    return cost_arr[1:]


arr = dijkstra(1)
print(max(dijkstra(arr.index(max(arr)) + 1)))
