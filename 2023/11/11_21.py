# 1572 중앙값
import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (4 * 65537)  # 0부터 65537까지로 이루어진 segment tree


def update(start, end, node, idx, val):  # 숫자가 들어왔을 때 해당 범위 값을 늘림
    if (idx < start) | (idx > end):
        return
    segment_tree[node] += val
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, val)
    update(mid + 1, end, node * 2 + 1, idx, val)


def get_middle(start, end, node, val):  # val번째 숫자를 구함
    if start == end:
        return start
    mid = (start + end) // 2
    if segment_tree[node * 2] >= val:
        return get_middle(start, mid, node * 2, val)
    else:
        return get_middle(mid + 1, end, node * 2 + 1, val - segment_tree[node * 2])


middle = (K + 1) // 2
deq = deque()  # 현재 슬라이드에 있는 숫자들
ans = 0
for i in range(N):
    curr = int(sys.stdin.readline())
    deq.append(curr)
    update(0, 65536, 1, curr, 1)  # 숫자가 들어왔을 떄 해당 범위를 1씩 증가
    if i >= K - 1:
        ans += get_middle(0, 65536, 1, middle)  # 중앙값을 구함
        last = deq.popleft()
        update(0, 65536, 1, last, -1)  # 숫자가 나갈 때 해당 범위를 1씩 감소

print(ans)
