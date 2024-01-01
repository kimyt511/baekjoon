import sys
import itertools
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
combination = [i for i in itertools.combinations(range(len(str(N))), 2)]


def exchange(num, i, j):
    _arr = list(str(num))
    _arr[i], _arr[j] = _arr[j], _arr[i]
    if _arr[0] == "0":
        return -1
    else:
        return int("".join(_arr))


deq = deque()
deq.append((N, K))
maximum = -1
dp = {}
while deq:
    num, k = deq.popleft()
    if (num, k) not in dp:
        dp[(num, k)] = 1
        if k != 0:
            for c in combination:
                exchange_num = exchange(num, c[0], c[1])
                if exchange_num != -1:
                    if (exchange_num, k - 1) not in dp:
                        deq.append((exchange_num, k - 1))
        else:
            maximum = max(maximum, num)

print(maximum)
