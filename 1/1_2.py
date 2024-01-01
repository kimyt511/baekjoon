# 1275 커피숍2
# 그냥 세그먼트 트리
import sys

N, Q = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * 4 * N


def build_tree(start, end, node):
    if start == end:
        segment_tree[node] = arr[start]
        return arr[start]
    else:
        mid = (start + end) // 2
        segment_tree[node] = build_tree(start, mid, node * 2) + build_tree(
            mid + 1, end, node * 2 + 1
        )
        return segment_tree[node]


def get_sum(start, end, node, left, right):
    if (start > right) | (end < left):
        return 0
    if (left <= start) & (end <= right):
        return segment_tree[node]
    mid = (start + end) // 2
    value = get_sum(start, mid, node * 2, left, right) + get_sum(
        mid + 1, end, node * 2 + 1, left, right
    )
    return value


def change_val(start, end, node, idx, val):
    if (start <= idx) & (idx <= end):
        segment_tree[node] += val
        if start < end:
            mid = (start + end) // 2
            change_val(start, mid, node * 2, idx, val)
            change_val(mid + 1, end, node * 2 + 1, idx, val)


build_tree(0, N - 1, 1)
for _ in range(Q):
    x, y, a, b = list(map(int, sys.stdin.readline().split()))
    start = min(x - 1, y - 1)
    end = max(x - 1, y - 1)
    a -= 1
    print(get_sum(0, N - 1, 1, start, end))
    change_val(0, N - 1, 1, a, b - arr[a])
    arr[a] = b
