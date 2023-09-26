import sys

R, C = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(R):
    arr.append(sys.stdin.readline()[:-1])


def check_arr_value(x, y):
    if (x in range(0, R)) & (y in range(0, C)):
        return arr[x][y]
    else:
        return -1


ld = [[0] * 808 for _ in range(808)]
rd = [[0] * 808 for _ in range(808)]
lu = [[0] * 808 for _ in range(808)]
ru = [[0] * 808 for _ in range(808)]
for i in range(R - 1, -1, -1):
    for j in range(C):
        if check_arr_value(i, j) == "1":
            ld[i][j] = ld[i + 1][j - 1] + 1
            rd[i][j] = ld[i + 1][j + 1] + 1
for i in range(R):
    for j in range(C):
        if check_arr_value(i, j) == "1":
            lu[i][j] = lu[i - 1][j - 1] + 1
            ru[i][j] = lu[i - 1][j + 1] + 1
ans = 0
for i in range(R):
    for j in range(C):
        for k in range(min(ld[i][j], rd[i][j])):
            if (
                (check_arr_value(i + 2 * (k), j) == "1")
                & (lu[i + 2 * (k)][j] >= k + 1)
                & (ru[i + 2 * (k)][j] >= k + 1)
            ):
                ans = max(ans, k + 1)
        for k in range(min(ru[i][j], rd[i][j])):
            if (
                (check_arr_value(i, j + 2 * (k)) == "1")
                & (lu[i][j + 2 * (k)] >= k + 1)
                & (ld[i][j + 2 * (k)] >= k + 1)
            ):
                ans = max(ans, k + 1)
print(ans)
