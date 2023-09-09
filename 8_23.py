import sys
from collections import deque

piece = []

for i in range(5):
    line = sys.stdin.readline()
    for j in range(5):
        if line[j] == "*":
            piece.append((i, j))

answer = [
    [[0]],
    [[1, 1]],
    [[1, 1, 2]],
    [[1, 1, 2, 2], [1, 1, 1, 3], [1, 1, 1, 2], [2, 2, 2, 2]],
    [[1, 1, 1, 1, 4], [1, 2, 2, 2, 3], [1, 1, 2, 2, 2], [1, 1, 1, 2, 3]],
]


def arrToNum(arr):
    num = 0
    for cor in arr:
        num = num | (1 << (cor[0] * 5 + cor[1]))
    return num


def numToArr(num):
    arr = []
    for i in range(25):
        if num & (1 << i):
            arr.append((i // 5, i % 5))
    return arr


def cloneArr(arr):
    return [i for i in arr]


def countMaxPiece(arr):
    sum = []
    for cor in arr:
        count = 0
        for _cor in arr:
            if ((cor[0] == _cor[0]) & (abs(cor[1] - _cor[1]) == 1)) | (
                cor[1] == _cor[1]
            ) & (abs(cor[0] - _cor[0]) == 1):
                count = count + 1
        sum.append(count)
    sum.sort()
    return sum


def checkBoundary(x, y):
    return (x >= 0) & (x < 5) & (y >= 0) & (y < 5)


dic = {}
dic[arrToNum(piece)] = 1
deq = deque()
deq.append((piece, 0))

while len(deq) != 0:
    arr, move = deq.popleft()
    if countMaxPiece(arr) in answer[len(piece) - 1]:
        print(move)
        exit()
    else:
        for i in range(len(arr)):
            for v in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if checkBoundary(arr[i][0] + v[0], arr[i][1] + v[1]):
                    _arr = cloneArr(arr)
                    _arr[i] = (arr[i][0] + v[0], arr[i][1] + v[1])
                    if arrToNum(_arr) not in dic:
                        dic[arrToNum(_arr)] = 1
                        deq.append((_arr, move + 1))
