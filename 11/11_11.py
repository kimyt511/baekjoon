# 1510 이등변삼각형 -> 다시 풀어봐야 함
import sys
import math

N, M = list(map(int, sys.stdin.readline().split()))

dp = {}


def get_points(x, y, dx, dy):
    if (x, y, dx, dy) in dp:
        return dp[(x, y, dx, dy)]
    y_range = [(dy / dx) * (-x) + y, (dy / dx) * (M - 1 - x) + y]
    y_range.sort()
    x_range = [(dx / dy) * (-y) + x, (dx / dy) * (M - 1 - y) + x]
    x_range.sort()
    return 10


ans = 0
for i in range(N * M):
    for j in range(N * M):
        if i == j:
            continue
        cor_i = (i % M, i // M)
        cor_j = (j % M, j // M)
        d = (cor_i[1] - cor_j[1], cor_j[0] - cor_i[0])
        mid = ((cor_i[0] + cor_j[0]) / 2, (cor_i[1] + cor_j[1]) // 2)
        if d[0] == 0:
            if mid[0] == int(mid[0]):
                ans += N - 1
        elif d[1] == 0:
            if mid[1] == int(mid[1]):
                ans += M - 1
        else:
            gcd = math.gcd(d[0], d[1])
            d = (d[0] // gcd, d[1] // gcd)
            if (mid[0] != int(mid[0])) & (mid[1] != int(mid[1])):
                if abs(d[0]) == abs(d[1]):
                    ans += get_points(int(mid[0]), int(mid[1]), d[0], d[1])
            elif mid[0] != int(mid[0]):
                if d[1] % 2 == 0:
                    _y = mid[1] + d[1] // 2
                    _x = (d[0] / d[1]) * (_y - mid[1]) + mid[0]
                    ans += get_points(_x, _y, d[0], d[1])
            elif mid[1] != int(mid[1]):
                if d[0] % 2 == 0:
                    _x = mid[0] + d[0] // 2
                    _y = (d[1] / d[0]) * (_x - mid[0]) + mid[1]
                    ans += get_points(_x, _y, d[0], d[1])
            else:
                ans += get_points(mid[0], mid[1], d[0], d[1]) - 1
print(ans)
