# 1194 달이 차오른다, 가자.

import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
board = [[0] * N for _ in range(M)]
end_arr = []
for i in range(N):
    line = sys.stdin.readline()[:-1]
    for j in range(M):
        if line[j] == "#":
            board[j][i] = 1
        elif line[j] == "0":
            start = (j, i)
        elif line[j] == "1":
            end_arr.append((j, i))
        elif line[j].isalpha():
            board[j][i] = line[j]

key_dic = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
}


def check_avaliable(x, y, keys):  # 해당 좌표가 접근 가능한지, 문이있다면, 열쇠가 있는지 확인
    if (x < 0) | (x >= M) | (y < 0) | (y >= N):
        return False
    if board[x][y] == 1:
        return False
    elif str(board[x][y]).isupper():
        if keys & (1 << key_dic[board[x][y]]):
            return True
        else:
            return False
    return True


dic = {}
deq = deque([(start[0], start[1], 0, 0)])
while deq:
    x, y, time, keys = deq.popleft()
    if (x, y, keys) not in dic:
        if (x, y) in end_arr:
            print(time)
            exit()
        if str(board[x][y]).islower():  # 도달 좌표에 열쇠가 있다면, 습득
            keys |= 1 << key_dic[board[x][y]]
        dic[(x, y, keys)] = time
        for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if check_avaliable(x + v[0], y + v[1], keys):
                if (x + v[0], y + v[1], keys) not in dic:
                    deq.append((x + v[0], y + v[1], time + 1, keys))

print(-1)
