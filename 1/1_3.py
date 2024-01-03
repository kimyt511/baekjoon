# 1285 동전 뒤집기
# 모든 열을 뒤집을 경우의 수 2^20
# 그 상태에서 어떤 행을 뒤집을지는 gridy로 결정 20^2
import sys
from collections import deque

N = int(sys.stdin.readline())
board = 0
for i in range(N):
    line = sys.stdin.readline()[:-1]
    for j in range(N):
        if line[j] == "T":
            board |= 1 << (i * N + j)


def count(string):
    val = 0
    for i in range(N):
        for j in range(N):
            if string & (1 << (i * N + j)):
                val += 1

    return val


ans = count(board)
deq = deque([(board, 0)])
board_arr = []
while deq:
    string, num = deq.popleft()
    if num == N:
        board_arr.append(string)
    else:
        deq.append((string, num + 1))
        for i in range(N):
            string ^= 1 << (num * N + i)
        deq.append((string, num + 1))


for board in board_arr:
    for i in range(N):
        num = 0
        for j in range(N):
            if board & (1 << (i + j * N)):
                num += 1
        if num >= N // 2:
            for j in range(N):
                board ^= 1 << (i + j * N)
    ans = min(ans, count(board))


print(ans)
