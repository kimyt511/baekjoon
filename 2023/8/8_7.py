import sys

N = int(sys.stdin.readline())
arr = [0] * 3

for _ in range(N):
    r, g, b = list(map(int, sys.stdin.readline().split()))
    arr = [r + min(arr[1], arr[2]), g + min(arr[0], arr[2]), b + min(arr[0], arr[1])]

print(min(arr))
