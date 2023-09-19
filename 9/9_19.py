# 1113 수영장 만들기
import sys

N, M = list(map(int, sys.stdin.readline().split()))
board = [[] for _ in range(N)]
for i in range(N):
    for num in sys.stdin.readline()[:-1]:
        board[i].append(int(num))

water = [[0] * M for _ in range(N)]
while max([max(i) for i in water]) < 8:
    curr = [[1] * (M - 2) for _ in range(N - 2)]
    Flag = True
    while Flag:
        Flag = False
        for i in range(N - 2):
            for j in range(M - 2):
                if curr[i][j] == 1:
                    water_level = board[i + 1][j + 1] + water[i + 1][j + 1] + curr[i][j]
                    if any(
                        [
                            board[i + 1 + v[0]][j + 1 + v[1]]
                            + water[i + 1 + v[0]][j + 1 + v[1]]
                            + curr[i + v[0]][j + v[1]]
                            < water_level
                            if (i + v[0] in range(0, N - 2))
                            & (j + v[1] in range(0, M - 2))
                            else board[i + 1 + v[0]][j + 1 + v[1]]
                            + water[i + 1 + v[0]][j + 1 + v[1]]
                            < water_level
                            for v in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        ]
                    ):
                        curr[i][j] = 0
                        Flag = True
    if sum([sum(i) for i in curr]) == 0:
        break
    else:
        for i in range(N - 2):
            for j in range(M - 2):
                water[i + 1][j + 1] += curr[i][j]

print(sum([sum(i) for i in water]))
