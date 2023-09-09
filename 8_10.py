import sys

sys.setrecursionlimit(10**6)
N, M = list(map(int, sys.stdin.readline().split()))
board = []
for i in range(N):
    board.append(sys.stdin.readline())


def checkArea(x, y):
    if (x < 0) | (x >= N) | (y < 0) | (y >= M):
        return False
    elif board[x][y] == "H":
        return False
    else:
        return True


answer = 0
dp = [[0] * M for _ in range(N)]


def dfs(x, y, count, route):
    global answer
    if count > answer:
        answer = count
    if (x, y) in route:
        print(-1)
        exit()
    else:
        route.append((x, y))
    if dp[x][y] < count:
        dp[x][y] = count
    elif dp[x][y] >= count:
        return None
    num = int(board[x][y])
    arr = [(x - num, y), (x + num, y), (x, y - num), (x, y + num)]
    for _x, _y in arr:
        if checkArea(_x, _y):
            dfs(_x, _y, count + 1, [i for i in route])


dfs(0, 0, 1, [])
print(answer)
