# 1970 건배
# 쌓아나가는 dp
import sys

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N):  # 간격이 1일 때
    dp[i][i + 1] = 1 if arr[i - 1] == arr[i] else 0

for d in range(2, N):  # 간격이 2 이상일 때
    for i in range(1, N - d + 1):
        val = 1 if arr[i - 1] == arr[i + d - 1] else 0
        dp[i][i + d] = dp[i + 1][i + d - 1] + val
        for j in range(d):  # 가능한 모든 경우의 수를 탐색
            dp[i][i + d] = max(dp[i][i + d], dp[i][i + j] + dp[i + j + 1][i + d])

print(dp[1][N])
