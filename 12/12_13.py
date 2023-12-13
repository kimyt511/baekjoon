# 1948 임계경로
# 위상정렬을 활용
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
entry = [0] * (N + 1)
for i in range(M):
    start, end, time = list(map(int, sys.stdin.readline().split()))
    graph[start].append((end, time))
    entry[end] += 1
start_country, end_country = list(map(int, sys.stdin.readline().split()))

topology_sort = []
topology_stack = [start_country]

while topology_stack:  # 위상정렬
    curr = topology_stack.pop()
    topology_sort.append(curr)
    for c in graph[curr]:
        entry[c[0]] -= 1
        if entry[c[0]] == 0:
            topology_stack.append(c[0])

max_time = [0] * (N + 1)
route_arr = [[] for _ in range(N + 1)]
for curr in topology_sort:  # 정렬된 순열을 탐색하며, 해당 node에 도달할 수 있는 최대 시간과 역추적을 위해 이전 노드를 저장
    curr_time = max_time[curr]
    for c in graph[curr]:
        if curr_time + c[1] > max_time[c[0]]:
            max_time[c[0]] = curr_time + c[1]
            route_arr[c[0]] = [curr]
        elif curr_time + c[1] == max_time[c[0]]:
            route_arr[c[0]].append(curr)

stack = [end_country]
max_count = 0
visited = [0] * (N + 1)
while stack:  # 역추적을 통해 최대 시간을 사용하는 route가 사용하는 도로의 총 합을 구함
    curr = stack.pop()
    if visited[curr] == 0:
        visited[curr] = 1
        for c in route_arr[curr]:
            max_count += 1
            stack.append(c)

print(max_time[end_country])
print(max_count)
