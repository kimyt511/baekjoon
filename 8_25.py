import sys
from collections import deque

board = [[0] * 501 for _ in range(501)]
N = int(sys.stdin.readline())
for _ in range(N):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            board[i][j] = 1
M = int(sys.stdin.readline())
for _ in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            board[i][j] = -1


def checkBoundary(x, y):
    return (x >= 0) & (x <= 500) & (y >= 0) & (y <= 500)


deq = deque()
deq.append((0, 0, 0))
dic = {}
dic[(0, 0)] = 1
while len(deq) != 0:
    x, y, hp = deq.popleft()
    if (x == 500) & (y == 500):
        print(hp)
        exit()
    for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if checkBoundary(x + v[0], y + v[1]) & ((x + v[0], y + v[1]) not in dic):
            dic[(x + v[0], y + v[1])] = 1
            if board[x + v[0]][y + v[1]] == 0:
                deq.appendleft((x + v[0], y + v[1], hp))
            elif board[x + v[0]][y + v[1]] == 1:
                deq.append((x + v[0], y + v[1], hp + 1))

print(-1)
