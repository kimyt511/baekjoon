# 1222 홍준 프로그래밍 대회
import sys
import math

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
num_arr = [0] * 2000001
for i in arr:
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            num_arr[j] = num_arr[j] + 1
            num = int(i / j)
            if num != j:
                num_arr[num] = num_arr[num] + 1
print(max([i * num_arr[i] if num_arr[i] != 1 else -1 for i in range(2000001)]))
