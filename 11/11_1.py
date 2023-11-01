# 1321 군인
import sys
import math

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
tree = [-1] * ((2 ** (int(math.log2(N)) + 2)))


def generate_tree(start, end, node):  # 세그먼트 트리 형성
    if start == end:
        tree[node] = arr[start]
        return arr[start]
    mid = (start + end) // 2
    tree[node] = generate_tree(start, mid, node * 2) + generate_tree(
        mid + 1, end, node * 2 + 1
    )
    return tree[node]


def get_sum(start, end, node, left, right):  # 세그먼트 트리를 활용, left부터 right까지 합
    if (left > end) | (right < start):
        return 0
    elif (left <= start) & (end <= right):
        return tree[node]
    else:
        mid = (start + end) // 2
        return get_sum(start, mid, node * 2, left, right) + get_sum(
            mid + 1, end, node * 2 + 1, left, right
        )


def update_value(
    start, end, node, index, value
):  # index의 값에 value만큼의 변화가 생겼을 때, tree를 update
    if (index < start) | (index > end):
        return 0
    tree[node] += value
    if start != end:
        mid = (start + end) // 2
        update_value(start, mid, node * 2, index, value)
        update_value(mid + 1, end, node * 2 + 1, index, value)
        return 0


def binary_search(
    start, end, value
):  # 이진탐색을 통해 값을 구함, 같은 값이 연속적으로 나올 땐 가장 앞에 있는 값을 return
    if end - start <= 1:
        start_sum = get_sum(0, N - 1, 1, 0, start)
        if start_sum >= value:
            return start
        else:
            return end
    mid = (start + end) // 2
    mid_sum = get_sum(0, N - 1, 1, 0, mid)
    if mid_sum < value:
        return binary_search(mid, end, value)
    else:
        return binary_search(start, mid, value)


M = int(sys.stdin.readline())
generate_tree(0, N - 1, 1)
for _ in range(M):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        update_value(0, N - 1, 1, command[1] - 1, command[2])
    elif command[0] == 2:
        print(binary_search(0, N - 1, command[1]) + 1)
