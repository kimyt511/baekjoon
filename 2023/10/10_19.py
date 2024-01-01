# 1014 컨닝
import sys
from collections import deque

C = int(sys.stdin.readline())


def cheating():
    N, M = list(map(int, sys.stdin.readline().split()))
    board = [[0] * M for _ in range(N)]
    for i in range(N):
        string = sys.stdin.readline()
        for j in range(M):
            if string[j] == "x":
                board[i][j] = 1
    dic = {}

    def put_student(arr, index):
        if index == N:
            return 0
        if (arr, index) in dic:
            return dic[(arr, index)]
        possible_arr = [i for i in board[index]]
        for i in range(M):
            if arr & (1 << i):
                if i - 1 in range(M):
                    possible_arr[i - 1] = 1
                if i + 1 in range(M):
                    possible_arr[i + 1] = 1
        _arr = []
        deq = deque()
        deq.append((0, 0, 0))
        while deq:
            students_arr, idx, count = deq.pop()
            if idx == M:
                _arr.append((students_arr, count))
            else:
                if possible_arr[idx] == 1:
                    deq.append((students_arr, idx + 1, count))
                else:
                    deq.append((students_arr, idx + 1, count))
                    if idx != 0:
                        if students_arr & (1 << (idx - 1)) == 0:
                            deq.append((students_arr | (1 << idx), idx + 1, count + 1))
                    else:
                        deq.append((students_arr | (1 << idx), idx + 1, count + 1))
        answer = 0
        for i in _arr:
            answer = max(answer, put_student(i[0], index + 1) + i[1])
        dic[(arr, index)] = answer
        return answer

    print(put_student(0, 0))


for _ in range(C):
    cheating()
