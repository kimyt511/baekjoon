import sys
import itertools
import math
from functools import reduce

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append((int(sys.stdin.readline())))
K = int(sys.stdin.readline())
arr = [(int(i % K), len(str(i))) for i in arr]
total_len = reduce(lambda acc, cur: acc + cur[1], arr, 0)
ten_mod = []
ten = 1
for _ in range(total_len + 1):
    ten_mod.append(ten % K)
    ten = ten * 10
total = math.factorial(N)
dp = [[-1] * K for _ in range(1 << N)]


def dfs(num, length, perm_len, mod):
    if (length == N) & (mod == 0):
        return 1
    else:
        if dp[num][mod] != -1:
            return dp[num][mod]
        else:
            ret = 0
            for i in range(N):
                if num & (1 << i) == 0:
                    ret = ret + dfs(
                        num | (1 << i),
                        length + 1,
                        perm_len + arr[i][1],
                        (mod + ten_mod[perm_len] * arr[i][0]) % K,
                    )
            dp[num][mod] = ret
            return ret


count = dfs(0, 0, 0, 0)
gcd = math.gcd(count, total)

print("{0}/{1}".format(int(count / gcd), int(total / gcd)))
