# 1708 볼록 껍질

import sys

N = int(sys.stdin.readline())
point_arr = []
for _ in range(N):
    point = list(map(int, sys.stdin.readline().split()))
    point_arr.append((point[0], point[1]))
point_arr.sort()  # point arr 정렬 후, 첫 번째 점인 기준점에 대한 기울기에 대해 다시 한 번 정렬
incline_arr = []
for i in range(1, N):
    if point_arr[0][0] == point_arr[i][0]:
        incline_arr.append((sys.maxsize, i))
    else:
        incline = (point_arr[i][1] - point_arr[0][1]) / (
            point_arr[i][0] - point_arr[0][0]
        )
        incline_arr.append((incline, i))
incline_arr.sort()
stack = [point_arr[0], point_arr[incline_arr[0][1]]]  # stack에 첫 두 점을 넣음
idx = 1
while idx < N - 1:
    if len(stack) < 2:
        stack.append(point_arr[incline_arr[idx][1]])
    else:  # stack의 마지막 두 점에 대해, 다음 점이 반시계 방향에 위치할 경우, stack에 추가, 아니면, 마지막 점을 pop하고, 다시 진행
        vector1 = ((stack[-2][0] - stack[-1][0]), (stack[-2][1] - stack[-1][1]))
        vector2 = (
            (point_arr[incline_arr[idx][1]][0] - stack[-1][0]),
            (point_arr[incline_arr[idx][1]][1] - stack[-1][1]),
        )
        if vector1[0] * vector2[1] - vector1[1] * vector2[0] < 0:
            stack.append(point_arr[incline_arr[idx][1]])
            idx += 1
        elif vector1[0] * vector2[1] - vector1[1] * vector2[0] == 0:
            stack.pop()
            stack.append(point_arr[incline_arr[idx][1]])
            idx += 1
        else:
            stack.pop()

print(len(stack))
