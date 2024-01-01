# 1169 정사각형 진열
import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = deque([[0, 0, arr[0] * 2]])
right_stack = deque([[0, arr[0] * 2, arr[0]]])
bn = arr[0]


def put_range(idx, left, right):
    while stack:
        if stack[0][2] <= left:
            break
        elif stack[0][2] >= right:
            return
        elif (stack[0][2] >= left) & (stack[0][1] < left):
            if arr[stack[0][0]] < arr[idx]:
                stack[0][2] = left
                break
            else:
                stack.appendleft([idx, stack[0][2], right])
                return
        elif stack[0][1] >= left:
            stack.popleft()
    stack.appendleft([idx, left, right])
    return


def maintain_stack(i, x, y):
    while right_stack:
        if right_stack[0][1] + right_stack[0][2] <= x + y:
            right_stack.popleft()
        else:
            break
    right_stack.appendleft([i, x, y])
    return


def get_bn(i):
    for c in right_stack:
        if arr[c[0]] < arr[i]:
            bn = c[1] + arr[c[0]]
        else:
            bn = c[1] - arr[c[0]] + arr[i] * 2
        if check_bn(bn, arr[i]):
            return bn
    return "fds"


def check_bn(bn, len):
    for c in right_stack:
        if c[1] + arr[c[0]] > bn:
            if bn - c[1] + arr[c[0]] < len * 2:
                return False
    return True


for i in range(1, N):
    if arr[i - 1] > arr[i]:
        bn = bn + arr[i] * 2
    else:
        bn = get_bn(i)
    put_range(i, bn - arr[i], bn + arr[i])
    maintain_stack(i, bn + arr[i], arr[i])
answer = []
while stack:
    i, _, _ = stack.pop()
    answer.append(i + 1)

print(*answer)
