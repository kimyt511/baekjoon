import sys

L, K, C = list(map(int, sys.stdin.readline().split()))
cuttingPosition = list(map(int, sys.stdin.readline().split()))
cuttingPosition.append(0)
cuttingPosition.sort()


def minSizeSearch(start, end):
    if start + 1 >= end:
        if check(start) != -1:
            return start
        else:
            return end
    mid = (start + end) // 2
    if check(mid) != -1:
        end = mid
    else:
        start = mid
    return minSizeSearch(start, end)


def check(num):
    curr = L - num
    count = 0
    val = 0
    for i in range(K):
        if cuttingPosition[K - i] < curr:
            return -1
        if cuttingPosition[K - i - 1] < curr:
            curr = cuttingPosition[K - i] - num
            val = cuttingPosition[K - i]
            count = count + 1
            if count > C:
                return -1
    if curr <= 0:
        if count < C:
            return cuttingPosition[1]
        else:
            return val
    else:
        return -1


num = minSizeSearch(1, L)
print(num, check(num))
