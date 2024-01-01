# 1539 이진 검색 트리
import sys
from sortedcontainers import SortedSet  # tree set 그러나 백준에서는 지원하지 않음

N = int(sys.stdin.readline())
ans = 0
heap = SortedSet()
height_arr = [-1] * N

for i in range(N):
    num = int(sys.stdin.readline())
    if i == 0:  # root일 때는 1을 더함
        ans += 1
        height_arr[num] = 1
        heap.add(num)
        continue
    if num < heap[0]:  # 가장 작은 숫자가 들어왔을 때는, 현재 가장 작은 숫자의 node의 left로 들어감
        ans += height_arr[heap[0]] + 1
        height_arr[num] = height_arr[heap[0]] + 1
        heap.add(num)
    elif num > heap[i - 1]:  # 가장 큰 숫자가 들어왔을 때는, 현재 가장 큰 숫자의 node의 right로 들어감
        ans += height_arr[heap[i - 1]] + 1
        height_arr[num] = height_arr[heap[i - 1]] + 1
        heap.add(num)
    else:  # 둘 다 아닌 경우, lower bound와 higher bound 중, height가 높은 node의 자식이 된다.
        start, end = 0, i - 1
        while end - start > 1:
            mid = (start + end) // 2
            if heap[mid] < num:
                start = mid
            else:
                end = mid
        height_arr[num] = max(height_arr[heap[start]], height_arr[heap[end]]) + 1
        ans += height_arr[num]
        heap.add(num)

print(ans)
