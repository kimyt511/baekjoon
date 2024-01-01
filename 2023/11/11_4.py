# 1369 배열값
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
prime_dic = [-1] * 1000001


def prime_factor(n):  # N의 숫자를 소인수분해했을 때 2와 5의 갯수
    if n == 0:
        return (0, 0)
    if prime_dic[n] != -1:
        return prime_dic[n]
    if n % 2 == 0:
        a, b = prime_factor(n // 2)
        prime_dic[n] = (a + 1, b)
        return (a + 1, b)
    elif n % 5 == 0:
        a, b = prime_factor(n // 5)
        prime_dic[n] = (a, b + 1)
        return (a, b + 1)
    else:
        prime_dic[n] = (0, 0)
        return (0, 0)


dp = [
    [[0] * 2 for _ in range(N)] for _ in range(N)
]  # dp[i][j][0]은 i,j칸까지 2의 갯수의 최소값, dp[i][j][1]은 5의 갯수의 최솟값


def check_idx(a, b):  # a,b가 존재하는 idx인지, 또는 arr[a][b]가 0이 아닌지 확인
    if (a < 0) | (b < 0):
        return False
    if arr[a][b] == 0:
        return False
    if dp[a][b][0] == 0:
        return False
    else:
        return True


for i in range(N):
    for j in range(N):
        if (i == 0) & (j == 0):
            dp[0][0][0] = prime_factor(arr[i][j])
            dp[0][0][1] = prime_factor(arr[i][j])
            continue
        a, b = prime_factor(arr[i][j])
        _arr = []
        if check_idx(i - 1, j):
            _arr.append((a + dp[i - 1][j][0][0], b + dp[i - 1][j][0][1]))
            _arr.append((a + dp[i - 1][j][1][0], b + dp[i - 1][j][1][1]))
        if check_idx(i, j - 1):
            _arr.append((a + dp[i][j - 1][0][0], b + dp[i][j - 1][0][1]))
            _arr.append((a + dp[i][j - 1][1][0], b + dp[i][j - 1][1][1]))
        if len(_arr) == 0:
            continue
        _arr.sort(key=lambda x: x[0])
        dp[i][j][0] = (_arr[0][0], _arr[0][1])
        _arr.sort(key=lambda x: x[1])
        dp[i][j][1] = (_arr[0][0], _arr[0][1])
print(min(min(dp[N - 1][N - 1][0]), min(dp[N - 1][N - 1][1])))
