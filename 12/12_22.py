# 1974 Jump Jump Championship
# LIS 알고리즘을 이분탐색을 활용, O(NlogN)으로 구현
# 반례를 찾지 못함
# idx를 backtracking으로도 구현해 봤으나, 채점결과 동일
import sys
from bisect import bisect_left

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [1]
    lower_bound_arr = [arr[0]]
    ans = [1]

    for i in range(1, N):
        if arr[i] > lower_bound_arr[-1]:
            lower_bound_arr.append(arr[i])
            ans.append(i + 1)
            dp.append(dp[-1] + 1)
        else:
            idx = bisect_left(lower_bound_arr, arr[i])
            if lower_bound_arr[idx] != arr[i]:
                lower_bound_arr[idx] = arr[i]
                ans[idx] = i + 1
    print(len(ans))
    print(*ans)
