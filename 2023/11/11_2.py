# 1328 고층 빌딩
import sys
import math
N, L, R = list(map(int, sys.stdin.readline().split()))

dp = {}
combination_dp = {}
def pick_group(n,c): # 조합을 계산하는 함수
    if (n,c) in combination_dp:
        return combination_dp[(n,c)]
    value = math.factorial(n) // math.factorial(c) // math.factorial(n-c)
    if value >= 1000000007:
        value %= 1000000007
    combination_dp[(n,c)] = value
    return value
def get_value(n,p): # n개의 숫자를 배열 할 때에 maximum value가 갱신되는 횟수가 p일 경우의 수
    if n == p:
        return 1
    if p == 1:
        return math.factorial(n-1)
    if p == 0:
        return 0
    if (n,p) in dp:
        return dp[(n,p)]
    value = 0
    for i in range(p, n+1): # dp를 활용, 최대값인 n이 위치할 수 있는 곳을 한정한 뒤에, 각 경우의 수를 구하여 더함
        value += get_value(i-1, p-1) * math.factorial(n-i) * pick_group(n-1, i-1)
        if value >= 1000000007:
            value %= 1000000007
    dp[(n,p)] = value
    return value
if L + R > N+1:
    print(0)
    exit()
value = 0
for i in range(L, N-R+2): # 최대값인 N이 위치할 수 있는 곳을 한정한 뒤에, 각 경우의 수를 구하여 더함
    value += get_value(i-1, L-1) * get_value(N-i,R-1) * pick_group(N-1, i-1)
    if value >= 1000000007:
        value %= 1000000007
print(value)