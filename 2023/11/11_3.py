# 1353 합과 곱
import sys
import math

S, P = map(int, sys.stdin.readline().split())
if S == P:
    print(1)
    exit()


def f(x, y):
    return math.pow(x / y, y)


n = -1
for i in range(2, S + 1):
    if f(S, i) >= P:  # 산술 기하 공식을 통해, (S/n)^n이 P보다 커지는 n의 최솟값을 구함
        n = i
        break
print(n)
