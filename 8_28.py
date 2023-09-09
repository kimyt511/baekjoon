import sys
import heapq

N, M = list(map(int, sys.stdin.readline().split()))


def checkBoundary(x, y):
    return (x >= 0) & (x < N) & (y >= 0) & (y < M)


forest = [[0] * M for _ in range(N)]
near_trash = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cost_arr = [[(sys.maxsize, sys.maxsize)] * M for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline()
    for j in range(M):
        if line[j] == ".":
            forest[i][j] = 0
        elif line[j] == "g":
            forest[i][j] = 1
            for v in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if checkBoundary(i + v[0], j + v[1]):
                    if near_trash[i + v[0]][j + v[1]] == 0:
                        near_trash[i + v[0]][j + v[1]] = 1
            near_trash[i][j] = 2

        elif line[j] == "S":
            start = (i, j)
            near_trash[i][j] = -1
        elif line[j] == "F":
            end = (i, j)
            near_trash[i][j] = -1
heap = []
heapq.heappush(heap, (0, 0, start))
while heap:
    trash, neartrash, cos = heapq.heappop(heap)
    if visited[cos[0]][cos[1]] == 0:
        cost_arr[cos[0]][cos[1]] = min(cost_arr[cos[0]][cos[1]], (trash, neartrash))
        visited[cos[0]][cos[1]] = 1
        for v in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if checkBoundary(cos[0] + v[0], cos[1] + v[1]):
                if visited[cos[0] + v[0]][cos[1] + v[1]] == 0:
                    is_near_trash = (
                        1 if near_trash[cos[0] + v[0]][cos[1] + v[1]] == 1 else 0
                    )
                    heapq.heappush(
                        heap,
                        (
                            trash + forest[cos[0] + v[0]][cos[1] + v[1]],
                            neartrash + is_near_trash,
                            (cos[0] + v[0], cos[1] + v[1]),
                        ),
                    )
answer = cost_arr[end[0]][end[1]]
print(answer[0], answer[1])
