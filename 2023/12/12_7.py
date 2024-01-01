# 1849 순열
# segment tree와 이분탐색을 통해 O(NlogNlogN)으로 구현, but 추가시간 없음으로 인해 시간초과
# C++으로 구현
import sys

N = int(sys.stdin.readline())
segment_tree = [0] * 400000


def update(start, end, node, idx, val):
    if start == end:
        if start == idx:
            segment_tree[node] += val
            return
    if start <= idx <= end:
        segment_tree[node] += val
        mid = (start + end) // 2
        update(start, mid, node * 2, idx, val)
        update(mid + 1, end, node * 2 + 1, idx, val)


def get(start, end, node, left, right):
    if (end < left) | (start > right):
        return 0
    if (left <= start) & (end <= right):
        return segment_tree[node]
    mid = (start + end) // 2
    return get(start, mid, node * 2, left, right) + get(
        mid + 1, end, node * 2 + 1, left, right
    )


ans = [0] * N
for i in range(N):
    num = int(sys.stdin.readline())
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if mid - get(0, N - 1, 1, 0, mid) < num:
            left = mid + 1
        else:
            right = mid - 1
    ans[left] = i + 1
    update(0, N - 1, 1, left, 1)

for i in ans:
    print(i)
