import sys

C, D, M = list(map(int, sys.stdin.readline().split()))
data = []
for _ in range(C):
    data.append(list(map(int, sys.stdin.readline().split())))
# day 수 만큼 knapsack 알고리즘을 실행
curr = M
for i in range(D - 1):
    option_arr = [(j[i], j[i + 1]) for j in data]  # 사는 비용이 투입 비용, 파는 비용이 얻는 비용
    dp = [c for c in range(curr + 1)]
    for c in range(curr + 1):
        value = c  # 아예 구매하지 않을 수 있으니 초기 값은 초기비용으로 세팅
        for option in option_arr:
            if option[0] <= c:
                value = max(value, dp[c - option[0]] + option[1])
        dp[c] = value
    curr = dp[curr]

print(curr)
