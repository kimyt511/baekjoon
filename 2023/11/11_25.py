# 1601 바이너리 파워 비숍
# 재귀로 구현
# O(n)이지만, 시간초과
import sys
import math

x, y = list(map(int, sys.stdin.readline().split()))
MAX_BIT = int(math.log2(max(x, y)) + 1)
dp = {}


def dfs(curr_x, curr_y, bit):
    if (curr_x == 0) & (curr_y == 0):
        return 0
    elif bit < 0:
        return -1
    move = 1 << bit
    next_x = curr_x - move if curr_x >= 0 else curr_x + move
    next_y = curr_y - move if curr_y >= 0 else curr_y + move

    val1 = dfs(next_x, next_y, bit - 1)
    if val1 != -1:
        val1 += 1
    val2 = dfs(curr_x, curr_y, bit - 1)
    if (val1 == -1) & (val2 == -1):
        return -1

    if (val2 == -1) | ((val1 != -1) & (val1 < val2)):
        dp[(curr_x, curr_y)] = (next_x, next_y)
    return val1 if (val2 == -1) | ((val1 != -1) & (val1 < val2)) else val2


ans = dfs(x, y, MAX_BIT)
if ans == -1:
    print(-1)
else:
    print(ans)
    arr = []
    curr_x, curr_y = x, y
    while (curr_x != 0) & (curr_y != 0):
        arr.append(dp[(curr_x, curr_y)])
        curr_x, curr_y = dp[(curr_x, curr_y)]
    arr.reverse()
    for i in arr:
        print(i[0], i[1])
    print(x, y)
