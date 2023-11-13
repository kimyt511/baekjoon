# 1517 버블 소트
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0


def divide(arr, length):  # 배열을 절반으로 나눈 뒤, 이를 합친다
    if length == 1:
        return arr
    mid = length // 2
    return merge(divide(arr[:mid], mid), divide(arr[mid:], length - mid), length)


def merge(arr1, arr2, length):  # 두 개의 정렬된 배열을 하나로 합친다.
    global ans  # arr2의 값이 result_arr로 들어올 때마다 남은 arr1의 길이만큼 swap이 발생
    result_arr = []
    length_count = 0
    arr1_point = 0
    arr2_point = 0
    mid = length // 2
    while length_count != length:
        if arr1_point == mid:
            while arr2_point != length - mid:
                result_arr.append(arr2[arr2_point])
                arr2_point += 1
            break
        elif arr2_point == length - mid:
            while arr1_point != mid:
                result_arr.append(arr1[arr1_point])
                arr1_point += 1
            break
        elif arr1[arr1_point] <= arr2[arr2_point]:
            result_arr.append(arr1[arr1_point])
            arr1_point += 1
            length_count += 1
        else:
            result_arr.append(arr2[arr2_point])
            arr2_point += 1
            length_count += 1
            ans += length // 2 - arr1_point
    return result_arr


divide(arr, N)
print(ans)
