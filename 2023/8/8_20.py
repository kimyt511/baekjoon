import sys
from collections import deque

M, N = list(map(int, sys.stdin.readline().split()))
maze = []

for _ in range(N):
    maze.append(sys.stdin.readline())

aoj = [[N * M] * M for _ in range(N)]
deq = deque()
deq.append((0, 0, 0))


def checkArea(x, y):
    return (x >= 0) & (x < N) & (y >= 0) & (y < M)


while len(deq) != 0:
    x, y, cost = deq.popleft()
    for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if checkArea(x + v[0], y + v[1]):
            if aoj[x + v[0]][y + v[1]] > cost + int(maze[x + v[0]][y + v[1]]):
                aoj[x + v[0]][y + v[1]] = cost + int(maze[x + v[0]][y + v[1]])
                deq.append((x + v[0], y + v[1], cost + int(maze[x + v[0]][y + v[1]])))
if (N == 1) & (M == 1):
    print(0)
else:
    print(aoj[N - 1][M - 1])
