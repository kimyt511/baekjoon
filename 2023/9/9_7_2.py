import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(sys.stdin.readline()[0:N])
if N == 1:
    print(0)
    exit()
if (sum([i.count("Y") for i in graph]) < (2 * N - 2)) | any(
    [i == "N" * N for i in graph]
):
    print(-1)
    exit()

group = 0
node_arr = [0] * N
while sum(node_arr) != N:
    start = node_arr.index(0)
    deq = deque()
    deq.append(start)
    while deq:
        curr = deq.pop()
        if node_arr[curr] == 0:
            node_arr[curr] = 1
            for i in range(N):
                if (node_arr[i] == 0) & (graph[curr][i] == "Y"):
                    deq.append(i)
    group = group + 1

print(group - 1)
