import sys


N, K = list(map(int, sys.stdin.readline().split()))

count = 0
num = 1 << 25

while count != K:
    if N == 0:
        print(0)
        exit()
    if num & N:
        N = N - num
        count = count + 1
    num = num >> 1
if N == 0:
    print(0)
else:
    print((num * 4) - (N + num * 2))
