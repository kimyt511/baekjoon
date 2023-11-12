# 1511 숫자 만들기
import sys

arr = list(map(int, sys.stdin.readline().split()))
num_sum = sum(arr)


def get_maxValue_idx(
    value, arr
):  # 해당 arr에서 가장 큰 값을 가지는 idx. 뒤에서부터 세기 때문에 가능한 큰 idx가 나온다
    for i in range(9, -1, -1):
        if arr[i] == value:
            return i
    return -1


def get_max_idx_notZero(arr, last):  # 해당 arr에서 last가 아니며, arr 값이 0이 아닌 가장 큰 idx
    for i in range(9, -1, -1):
        if (arr[i] != 0) & (i != last):
            return i
    return -1


curr = ""
last_num = -1
while num_sum > 0:
    max_value_idx = get_maxValue_idx(max(arr), arr)
    if (
        max_value_idx == last_num
    ):  # max_value가 마지막 숫자이거나, 총 숫자의 절반 이상을 차지하지 않으면, 가능한 가장 큰 idx를 추가
        max_value_idx = get_max_idx_notZero(arr, last_num)
    elif arr[max_value_idx] <= num_sum - arr[max_value_idx]:
        max_value_idx = get_max_idx_notZero(arr, last_num)
    if max_value_idx == -1:  # 남은 arr의 숫자 중, 사용 가능한 값이 없는 경우 -> 남은 유일한 숫자가 마지막에 사용한 경우
        break
    curr += str(max_value_idx)  # 그게 아니라면, 기존 max_value_idx를 그대로 사용
    arr[max_value_idx] -= 1
    num_sum -= 1
    last_num = max_value_idx

print(int(curr))
