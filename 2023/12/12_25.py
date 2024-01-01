# 1989 부분배열 고르기2
# 부분합은 세그먼트 트리를 활용, 최소값 구간은 monotone queue 활용
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sum_tree = [0] * 4 * N
min_tree = [0] * 4 * N


def build_sum_tree(start, end, node):
    if start == end:
        sum_tree[node] = arr[start]
        return arr[start]
    mid = (start + end) // 2
    sum_tree[node] = build_sum_tree(start, mid, node * 2) + build_sum_tree(
        mid + 1, end, node * 2 + 1
    )
    return sum_tree[node]


build_sum_tree(0, N - 1, 1)  # 부분합에 대한 segment tree 생성


def build_min_tree(start, end, node):
    if start == end:
        min_tree[node] = arr[start]
        return arr[start]
    mid = (start + end) // 2
    min_tree[node] = min(
        build_min_tree(start, mid, node * 2), build_min_tree(mid + 1, end, node * 2 + 1)
    )
    return min_tree[node]


# build_min_tree(0, N - 1, 1) 부분최소값에 대한 segment tree 생성, but 사용하지 않음


def search_sum_tree(start, end, node, left, right):
    if (start > right) | (end < left):
        return 0
    if (left <= start) & (end <= right):
        return sum_tree[node]
    mid = (start + end) // 2
    return search_sum_tree(start, mid, node * 2, left, right) + search_sum_tree(
        mid + 1, end, node * 2 + 1, left, right
    )


def search_min_tree(start, end, node, left, right):
    if (start > right) | (end < left):
        return sys.maxsize
    if (left <= start) & (end <= right):
        return min_tree[node]
    mid = (start + end) // 2
    return min(
        search_min_tree(start, mid, node * 2, left, right),
        search_min_tree(mid + 1, end, node * 2 + 1, left, right),
    )


left_monotone_queue = [
    N - 1
] * N  # monotone queue를 두 번 사용해서 해당 값이 최소값으로 존재할 수 있는 구간을 구함
right_monotone_queue = [0] * N

stack = []
for i in range(N):
    while stack:
        if stack[-1][0] > arr[i]:
            curr = stack.pop()
            left_monotone_queue[curr[1]] = i - 1
        else:
            break
    stack.append((arr[i], i))
stack = []
for i in range(N - 1, -1, -1):
    while stack:
        if stack[-1][0] > arr[i]:
            curr = stack.pop()
            right_monotone_queue[curr[1]] = i + 1
        else:
            break
    stack.append((arr[i], i))

ans = 0
curr = (1, 1)
for i in range(N):  # 세그먼트 트리와 monotone queue를 활용해 O(NlogN)으로 결과값 계산
    value = arr[i] * search_sum_tree(
        0, N - 1, 1, right_monotone_queue[i], left_monotone_queue[i]
    )
    if value > ans:
        ans = value
        curr = (right_monotone_queue[i] + 1, left_monotone_queue[i] + 1)

print(ans)
print(*curr)
