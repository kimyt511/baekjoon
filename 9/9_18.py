# 1060 좋은 수
import sys
import heapq

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
S.sort()
N = int(sys.stdin.readline())


def get_good_range(start, end, x):
    return (x - start + 1) * (end - x + 1) - 1


range_arr = []
start = 1
for i in range(L):
    range_arr.append((S[i] - start, start))
    start = S[i] + 1
heap = []
for i in range_arr:
    num = min(i[0], N)
    for j in range(int(num / 2)):
        heapq.heappush(
            heap, (get_good_range(i[1], i[0] + i[1] - 1, j + i[1]), j + i[1])
        )
        heapq.heappush(
            heap,
            (
                get_good_range(i[1], i[0] + i[1] - 1, i[0] + i[1] - 1 - j),
                i[0] + i[1] - 1 - j,
            ),
        )
    if num % 2 == 1:
        heapq.heappush(
            heap,
            (
                get_good_range(i[1], i[0] + i[1] - 1, int((num - 1) / 2) + i[1]),
                int((num - 1) / 2) + i[1],
            ),
        )

for i in range(L):
    heapq.heappush(heap, (0, S[i]))

if N <= max(S):
    arr = []
    for i in range(N):
        _, num = heapq.heappop(heap)
        arr.append(str(num))
    print(" ".join(arr))
else:
    arr = []
    while heap:
        _, num = heapq.heappop(heap)
        arr.append(str(num))
    for i in range(max(S) + 1, N + 1):
        arr.append(str(i))
    print(" ".join(arr))
