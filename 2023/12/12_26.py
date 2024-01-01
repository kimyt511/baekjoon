# 1175 배달
# BFS, DP
import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
board = [[1] * N for _ in range(M)]
c_arr = []
for i in range(N):
    line = sys.stdin.readline()
    for j in range(M):
        if line[j] == "S":
            start = (j, i)
        elif line[j] == "C":
            c_arr.append((j, i))
            board[j][i] = 2
        elif line[j] == "#":
            board[j][i] = 0


def check_avaliable(x, y):  # 해당 좌표가 이동가능한 좌표인지
    if (x < 0) | (x >= M) | (y < 0) | (y >= N):
        return False
    if board[x][y] == 0:
        return False
    return True


deq = deque([(start[0], start[1], 0, 0, -1)])
vec_dic = {0: (1, 0), 1: (-1, 0), 2: (0, 1), 3: (0, -1)}
dic = {}
while deq:
    x, y, time, visit, vector = deq.popleft()
    if (x, y, visit, vector) not in dic:
        if (x, y) == c_arr[0]:  # 방문한 좌표가 C일 때, visit 갱신
            visit |= 1 << 0
        if (x, y) == c_arr[1]:
            visit |= 1 << 1
        if visit == 3:
            print(time)
            exit()
        dic[(x, y, visit, vector)] = time
        for v in range(4):
            if vector != v:  # 지난번 방향과 일치하는지 확인
                curr_v = vec_dic[v]
                if check_avaliable(x + curr_v[0], y + curr_v[1]):
                    if (x + curr_v[0], y + curr_v[1], visit, vector) not in dic:
                        deq.append((x + curr_v[0], y + curr_v[1], time + 1, visit, v))

print(-1)
