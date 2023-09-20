# 1081 합
import sys

L, U = list(map(int, sys.stdin.readline().split()))


def sumWithLength(len):
    if len < 0:
        return 0
    else:
        return (10 ** (len - 1)) * len * 45


def sumZeroToNum(num):
    return int((num * (num + 1)) / 2)


def getRemainNums(num, i):
    if len(str(num)) > i + 1:
        return int(str(num)[i + 1 :])
    else:
        return 0


def sumAllNum(num):
    if num < 0:
        return 0
    sum = 0
    for i in range(len(str(num))):
        sum += int(
            int(str(num)[i]) * sumWithLength(len(str(num)) - i - 1)
            + sumZeroToNum(int(str(num)[i]) - 1) * (10 ** (len(str(num)) - i - 1))
            + int(str(num)[i]) * (getRemainNums(num, i) + 1)
        )
    return sum


print(sumAllNum(U) - sumAllNum(L - 1))
