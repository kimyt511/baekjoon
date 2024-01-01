import sys
from collections import deque
import itertools

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(sys.stdin.readline()[0:N])
if (sum([i.count("Y") for i in graph]) < (2 * N - 2)) | any(
    [i == "N" * N for i in graph]
):
    print(-1)
    exit()


def checkFullConnected(graph, num):
    node_arr = [0] * num
    deq = deque()
    deq.append(0)
    while deq:
        curr = deq.pop()
        if node_arr[curr] == 0:
            node_arr[curr] = 1
            for i in range(N):
                if (node_arr[i] == 0) & (graph[curr][i] == "Y"):
                    deq.append(i)
    return all([i == 1 for i in node_arr])


def checkChangeable(graph, a, b, c, d):
    return (
        (graph[a][b] == "Y")
        & (graph[c][d] == "Y")
        & (graph[a][c] == "N")
        & (graph[a][d] == "N")
        & (graph[b][c] == "N")
        & (graph[b][d] == "N")
    )


def changeVector(graph, a, b, c, d):
    case1 = [list(i) for i in graph]
    case2 = [list(i) for i in graph]
    case1[a][b], case1[b][a], case1[c][d], case1[d][c] = "N", "N", "N", "N"
    case2[a][b], case2[b][a], case2[c][d], case2[d][c] = "N", "N", "N", "N"
    case1[a][c], case1[c][a], case1[b][d], case1[d][b] = "Y", "Y", "Y", "Y"
    case2[a][d], case2[d][a], case2[b][c], case2[c][b] = "Y", "Y", "Y", "Y"
    case1 = ["".join(i) for i in case1]
    case2 = ["".join(i) for i in case2]
    return (case1, case2)


deq = deque()
deq.append((graph, 0))
combinations = [i for i in itertools.combinations(range(N), 4)]
dic = {}
answer = sys.maxsize
while deq:
    graph, changed = deq.popleft()
    print(graph, changed)
    if "".join(graph) not in dic:
        dic["".join(graph)] = 1
        if checkFullConnected(graph, N):
            answer = min(answer, changed)
        for i in combinations:
            if checkChangeable(graph, i[0], i[1], i[2], i[3]):
                case1, case2 = changeVector(graph, i[0], i[1], i[2], i[3])
                if "".join(case1) not in dic:
                    deq.appendleft((case1, changed + 1))
                if "".join(case2) not in dic:
                    deq.appendleft((case2, changed + 1))
            elif checkChangeable(graph, i[0], i[2], i[1], i[3]):
                case1, case2 = changeVector(graph, i[0], i[2], i[1], i[3])
                if "".join(case1) not in dic:
                    deq.appendleft((case1, changed + 1))
                if "".join(case2) not in dic:
                    deq.appendleft((case2, changed + 1))
            elif checkChangeable(graph, i[0], i[3], i[1], i[2]):
                case1, case2 = changeVector(graph, i[0], i[3], i[1], i[2])
                if "".join(case1) not in dic:
                    deq.appendleft((case1, changed + 1))
                if "".join(case2) not in dic:
                    deq.appendleft((case2, changed + 1))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
