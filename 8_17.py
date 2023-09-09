import sys

N = int(sys.stdin.readline())
arr = [0] * 1001
for num in list(map(int, sys.stdin.readline().split())):
    arr[num] = arr[num] + 1


def get_min(curr):
    for i in range(1001):
        if (i != (curr + 1)) & (arr[i] != 0):
            if check_num(i):
                arr[i] = arr[i] - 1
                return i


def check_num(num):
    if num == 1000:
        return True
    if arr[num + 1] != 0:
        if all(
            [
                arr[i] == 0 if (i != num) & (i != (num + 1)) else True
                for i in range(1001)
            ]
        ):
            return False
    return True


curr = -2
sorted_arr = []
for _ in range(N):
    curr = get_min(curr)
    sorted_arr.append(str(curr))

print(" ".join(sorted_arr))
