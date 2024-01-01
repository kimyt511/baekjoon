import sys
import heapq
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
crystal = []
bag = []
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(crystal, (arr[0], arr[1]))
for _ in range(K):
    heapq.heappush(bag, int(sys.stdin.readline()))

expensive = []

sum = 0
countK = K
countN = N
countE = 0
while countK > 0:
    bag_weight = heapq.heappop(bag)
    countK = countK - 1
    while countN > 0:
        weight, cost = heapq.heappop(crystal)
        if weight > bag_weight:
            heapq.heappush(crystal, (weight, cost))
            break
        else:
            countN = countN - 1
            heapq.heappush(expensive, -cost)
            countE = countE + 1
    if countE > 0:
        cost = heapq.heappop(expensive)
        countE = countE - 1
        sum = sum - cost

print(sum)
