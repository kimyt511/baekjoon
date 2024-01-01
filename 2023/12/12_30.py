# 1208 부분 수열의 합2
# 2^40의 시간 복잡도를 2^20 + 2^20으로 나누어 확인
import sys
from collections import deque

N, S = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

left_arr = arr[: N // 2]
right_arr = arr[N // 2 :]


def make_dic(arr):  # 모든 부분수열의 합으로 dic 구성
    dic = {}
    length = len(arr)
    deq = deque([(0, 0)])
    while deq:
        val, idx = deq.popleft()
        if idx == length:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        else:
            deq.append((val, idx + 1))
            deq.append((val + arr[idx], idx + 1))
    return dic


left_dic = make_dic(left_arr)
right_dic = make_dic(right_arr)
ans = 0

for i in left_dic.keys():  # 각 dic로 S가 만들어지는 경우의 수를 합침
    if S - i in right_dic:
        ans += left_dic[i] * right_dic[S - i]
if S == 0:  # 길이가 0인 부분수열의 예외 처리
    ans -= 1
print(ans)
