# 1053 펠린드롬 공장
import sys
from collections import deque
import itertools

line = sys.stdin.readline()[:-1]
length = len(line)
dp = [[-1] * length for _ in range(length)]


def get_dp(i, j, string):
    if i >= j:
        return 0
    if (i not in range(length)) | (j not in range(length)):
        return length
    if dp[i][j] != -1:
        return dp[i][j]

    value = min(
        [
            get_dp(i + 1, j, string) + 1,
            get_dp(i, j - 1, string) + 1,
            get_dp(i + 1, j - 1, string) + (string[i] != string[j]),
        ]
    )
    dp[i][j] = value
    return value


answer = get_dp(0, length - 1, line)
for i in itertools.combinations(range(length), 2):
    dp = [[-1] * length for _ in range(length)]
    arr = list(line)
    arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    answer = min(answer, get_dp(0, length - 1, "".join(arr)) + 1)

print(answer)
