# 1571 단어 굴리기
import sys
import math

N = int(sys.stdin.readline())
string_arr = []
for _ in range(N):
    string_arr.append(sys.stdin.readline()[:-1])
request = sys.stdin.readline()
request_arr = []
for i in range(N):
    if request[i] in string_arr[i]:
        request_arr.append(string_arr[i].index(request[i]))  # 현재 전광판의 몇번째 문자가 출력되어야 하는지
    else:
        print(-1)
        exit()
curr_len = len(string_arr[0])
curr_time = request_arr[0]
for i in range(1, N):  # n번째까지 걸린 시간 및 길이(최소공배수)와 n+1번째 전광판의 길이와 나올 문자의 순서를 통해
    next_len = len(string_arr[i])  # n+1번 전광판까지 길이(최소공배수)와 걸린 시간을 계산
    next_time = request_arr[i]
    lcm = math.lcm(curr_len, next_len)
    num = -1
    for j in range(lcm // curr_len):
        value = curr_len * j + curr_time - next_time
        if value < 0:
            continue
        if value % next_len == 0:
            num = curr_len * j + curr_time
    if num == -1:
        print(-1)
        exit()
    curr_len = lcm
    curr_time = num

print(curr_time)
