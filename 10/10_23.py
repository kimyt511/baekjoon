# 1160 random number generator
import sys

m, a, c, x, n, g = list(map(int, sys.stdin.readline().split()))


def multiple_matrix(a, b, c, d):
    val1 = a * c
    if val1 > m:
        val1 = val1 % m
    val2 = a * d + b
    if val2 > m:
        val2 = val2 % m
    return (val1, val2)


def recursion(a, c, n):
    if n == 1:
        return (a, c)
    if n % 2 == 0:
        _a, _c = recursion(a, c, n // 2)
        return multiple_matrix(_a, _c, _a, _c)
    elif n % 2 == 1:
        _a, _c = recursion(a, c, n // 2)
        val1, val2 = multiple_matrix(_a, _c, _a, _c)
        return multiple_matrix(val1, val2, a, c)


val1, val2 = recursion(a, c, n)
val1, val2 = val1 % m, val2 % m
value = (val1 * x + val2) % m
print(value % g)
