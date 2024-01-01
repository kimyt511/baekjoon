import sys

s, N, K, R1, R2, C1, C2 = list(map(int, sys.stdin.readline().split()))


def is_black(x, y, N, K, size):
    if size == 1:
        return 0
    elif size == N:
        if (x in range(int((N - K) / 2), int((N - K) / 2) + K)) & (
            y in range(int((N - K) / 2), int((N - K) / 2) + K)
        ):
            return 1
        else:
            return 0
    elif (int(x / (size / N)) in range(int((N - K) / 2), int((N - K) / 2) + K)) & (
        int(y / (size / N)) in range(int((N - K) / 2), int((N - K) / 2) + K)
    ):
        return 1
    else:
        return is_black(x % (size / N), y % (size / N), N, K, size / N)


for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        print(is_black(i, j, N, K, N**s), end="")
    print()
