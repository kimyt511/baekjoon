# 1048 유니콘
import sys
from collections import deque

N, M, L = list(map(int, sys.stdin.readline().split()))
string = sys.stdin.readline()
len_string = len(string) - 1
position_dictionary = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    position_dictionary[i] = []
board = []
for i in range(N):
    line = sys.stdin.readline()
    for j in range(M):
        position_dictionary[line[j]].append((i, j))
    board.append(line)


def get_acc_sum(arr, x, y, num, plus):
    if (x < 0) | (y < 0):
        return num
    x = min(N - 1, x)
    y = min(M - 1, y)
    num = num + arr[x][y] if plus else num - arr[x][y]
    return num % 1000000007


def get_acc_sum2(arr, x, y, num, plus):
    if (x in range(N)) & (y in range(M)):
        num = num + arr[x][y] if plus else num - arr[x][y]
        return num % 1000000007
    else:
        return num


def accum(arr, x1, y1, x2, y2):
    return arr[x2][y2] - arr[x1][y2] - arr[x2][y1] + arr[x1][y1]


def acc_sum(arr, idx):
    if idx == len_string:
        return sum([sum(i) for i in arr]) % 1000000007
    sum_list = [[sum(arr[i][: j + 1]) for j in range(M)] for i in range(N)]
    for i in range(N - 1):
        for j in range(M):
            sum_list[i + 1][j] += sum_list[i][j]
    _board = [[0] * M for _ in range(N)]
    for i in position_dictionary[string[idx]]:
        x, y = i[0], i[1]
        curr = sum_list[N - 1][M - 1]
        curr = get_acc_sum(sum_list, x + 1, M - 1, curr, False)
        curr = get_acc_sum(sum_list, x - 2, M - 1, curr, True)
        curr = get_acc_sum(sum_list, N - 1, y + 1, curr, False)
        curr = get_acc_sum(sum_list, N - 1, y - 2, curr, True)
        for j in [(x - 2, y - 2), (x + 2, y - 2), (x - 2, y + 2), (x + 2, y + 2)]:
            curr = get_acc_sum2(arr, j[0], j[1], curr, False)
        for j in range(3):
            for k in range(3):
                curr = get_acc_sum2(arr, x - 1 + j, y - 1 + k, curr, True)
        _board[x][y] = curr
    return acc_sum(_board, idx + 1)


_board = [[0] * M for _ in range(N)]
for i in position_dictionary[string[0]]:
    _board[i[0]][i[1]] = 1


print(acc_sum(_board, 1))
