# 1852 수 묶기
# 브루드포스로 해결
import sys

sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dic = {}


def bind_num(idx, arr):  # idx: 현재 줄 수 arr: 아직 묶이지 않은 수의 배열
    if (idx, arr) in dic:
        return dic[(idx, arr)]
    max_val, min_val = -1, sys.maxsize
    if idx == N - 1:
        if arr == (1 << 3) - 1:
            return (0, 0)
        elif arr == (1 << 0):
            val = abs(board[idx][1] - board[idx][2])
            return (val, val)
        elif arr == (1 << 2):
            val = abs(board[idx][0] - board[idx][1])
            return (val, val)
        else:
            return (max_val, min_val)
    if (arr & (1 << 0) == 0) & (arr & (1 << 1) == 0):
        if arr & (1 << 2) == 0:
            add_val = abs(board[idx][0] - board[idx][1]) + abs(
                board[idx][2] - board[idx + 1][2]
            )
            next_arr = bind_num(idx + 1, (1 << 2))
        else:
            add_val = abs(board[idx][0] - board[idx][1])
            next_arr = bind_num(idx + 1, 0)
        max_val = max(max_val, next_arr[0] + add_val)
        min_val = min(min_val, next_arr[1] + add_val)
    if (arr & (1 << 1) == 0) & (arr & (1 << 2) == 0):
        if arr & (1 << 0) == 0:
            add_val = abs(board[idx][1] - board[idx][2]) + abs(
                board[idx][0] - board[idx + 1][0]
            )
            next_arr = bind_num(idx + 1, (1 << 0))
        else:
            add_val = abs(board[idx][1] - board[idx][2])
            next_arr = bind_num(idx + 1, 0)
        max_val = max(max_val, next_arr[0] + add_val)
        min_val = min(min_val, next_arr[1] + add_val)
    add_val = 0
    next_val = 0
    for i in range(3):
        if arr & (1 << i) == 0:
            add_val += abs(board[idx][i] - board[idx + 1][i])
            next_val |= 1 << i
    next_arr = bind_num(idx + 1, next_val)
    max_val = max(max_val, next_arr[0] + add_val)
    min_val = min(min_val, next_arr[1] + add_val)

    dic[(idx, arr)] = (
        max_val,
        min_val,
    )  # 현재 줄에서 가능한 수 묶기 방법을 모두 고려, 현재 idx 밑으로 발생할 수 있는 값의 최대값과 최소값을 반환
    return (max_val, min_val)


ans = bind_num(0, 0)
print(ans[0])
print(ans[1])
