matrix = [[10] * 10 for _ in range(10)]
n = len(matrix)
dp = [[-1] * n for _ in range(n)]


def getVal(x, y):
    if (x < 0) | (x >= n):
        return 101
    if dp[x][y] != -1:
        return dp[x][y]
    if y == n - 1:
        return matrix[y][x]
    else:
        val = matrix[y][x] + min(
            [getVal(x - 1, y + 1), getVal(x, y + 1), getVal(x + 1, y + 1)]
        )
        dp[x][y] = val
        print(x, y, val)
        return val


print(min([getVal(i, 0) for i in range(n)]))
# print(dp)
