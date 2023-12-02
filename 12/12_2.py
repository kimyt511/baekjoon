# 1777 순열복원
# O(n*logn*logn)으로 구현, python에서는 시간 초과
# 이분탐색을 update 안에 넣어 O(n*logn)으로 구현 가능
import sys

N = int(sys.stdin.readline())
combination = list(map(int, sys.stdin.readline().split()))
seg_tree = [0] * 400000
visited = [-1] * N


def update(start, end, node, index, val):
    if start > end:
        return
    if index in range(start, end + 1):
        seg_tree[node] += val
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node * 2, index, val)
            update(mid + 1, end, node * 2 + 1, index, val)


def get(start, end, node, left, right):
    if (left > end) | (right < start):
        return 0
    if (left <= start) & (end <= right):
        return seg_tree[node]
    mid = (start + end) // 2
    return get(start, mid, node * 2, left, right) + get(
        mid + 1, end, node * 2 + 1, left, right
    )


for i in range(N):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if mid + 1 - get(0, N - 1, 1, 0, mid) < N - i - combination[N - 1 - i]:
            start = mid + 1
        else:
            end = mid - 1
    visited[start] = N - i
    update(0, N - 1, 1, start, 1)

print(*visited)
