# 1136 조각놓기
import sys

L, N = list(map(int, sys.stdin.readline().split()))
puzzles = list(map(int, sys.stdin.readline().split()))
puzzles.sort()
if puzzles[0] > L:
    print(0)
    exit()

puzzles_sum = sum(puzzles)
dic = [[-1] * (L + 1) for _ in range(N + 1)]
dic[0][0] = 0
for i in range(N):
    for j in range(N - 1, -1, -1):
        for s in range(L, -1, -1):
            if (dic[j][s] != -1) & (s + puzzles[i] <= L):
                if dic[j][s] == i:
                    dic[j + 1][s + puzzles[i]] = i + 1
                else:
                    dic[j + 1][s + puzzles[i]] = max(
                        dic[j + 1][s + puzzles[i]], dic[j][s]
                    )
for j in range(N):
    for s in range(L + 1):
        if dic[j][s] != -1:
            if L <= s + (j + 1) * puzzles[dic[j][s]] - 1:
                print(j)
                exit()

print(N)
