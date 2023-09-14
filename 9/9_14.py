# 1019 책 페이지
import sys

N = int(sys.stdin.readline())
num_arr = [0] * 10


def add_arr(arr1, arr2):
    for i in range(10):
        arr1[i] = arr1[i] + arr2[i]
    return arr1


def count_num_except_zero(num):
    arr = [int((num + 1) / 10 * len(str(num)))] * 10
    return arr


def count_num(str_num):
    if len(str_num) == 1:
        arr = [0] * 10
        for i in range(int(str_num) + 1):
            arr[i] += 1
        return arr
    else:
        arr = [0] * 10
        for i in range(int(str_num[0])):
            _arr = count_num_except_zero(int("9" * (len(str_num) - 1)))
            _arr[i] += int("9" * (len(str_num) - 1)) + 1
            arr = add_arr(arr, _arr)
        arr[int(str_num[0])] += int(str_num[1:]) + 1
        arr = add_arr(arr, count_num(str_num[1:]))
        return arr


arr = count_num(str(N))
arr[0] -= int("1" * len(str(N)))
print(" ".join(list(map(str, arr))))
