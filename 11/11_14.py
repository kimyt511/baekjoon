# 1521 랜덤소트
import sys
import itertools

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)
dp = {}

def get_E(arr):
    if arr == sorted_arr: # 현재 sorted arr일 때
        return 0
    if tuple(arr) in dp:
        return dp[tuple(arr)]
    count = 0
    sum_E = 0
    for c in itertools.combinations(range(N),2):
        if arr[c[0]] > arr[c[1]]: # sorted arr가 아닐 때, sort에 맞지 않는 pair을 교환, 해당 경우의 확률을 재귀적으로 구함
            _arr = [i for i in arr]
            _arr[c[0]], _arr[c[1]] = _arr[c[1]], _arr[c[0]]
            sum_E += get_E(_arr) + 1
            count += 1
    dp[tuple(arr)] = sum_E / count
    return sum_E / count

print(get_E(arr))