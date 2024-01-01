# 1207번 종이 자르기
import sys

L = int(sys.stdin.readline())
blocks = []
shop_num = 0
for i in range(5):
    N, M = list(map(int, sys.stdin.readline().split()))
    arr = [[0] * M for _ in range(N)]
    for j in range(N):
        line = sys.stdin.readline()
        for k in range(M):
            if line[k] == "#":
                arr[j][k] = 1
                shop_num = shop_num + 1
            else:
                arr[j][k] = 0
    blocks.append((N, M, arr, i + 1))
blocks.sort(reverse=True, key=lambda x: x[0] * x[1])
paper = [[0] * L for _ in range(L)]
if shop_num != L * L:
    print("gg")
    exit()


def putBlock(x, y, block, arr, num):
    _arr = [[j for j in i] for i in arr]
    len_x, len_y = len(block[0]), len(block)
    for i in range(len_y):
        for j in range(len_x):
            if block[i][j] == 1:
                if _arr[i + y][j + x] == 0:
                    _arr[i + y][j + x] = num
                else:
                    return -1
    return _arr


def deleteBlock(x, y, block, arr):
    len_x, len_y = len(block[0]), len(block)
    for i in range(len_y):
        for j in range(len_x):
            if block[i][j] == 1:
                arr[i + y][j + x] = 0
    return arr


answer_arr = []


def bruteForce(block_num):
    global paper
    if block_num >= 5:
        if all([all([j != 0 for j in i]) for i in paper]):
            answer_arr.append(["".join(list(map(str, i))) for i in paper])
    else:
        x, y = L - blocks[block_num][1] + 1, L - blocks[block_num][0] + 1
        for i in range(y):
            for j in range(x):
                next_arr = putBlock(
                    j, i, blocks[block_num][2], paper, blocks[block_num][3]
                )
                if next_arr != -1:
                    paper = next_arr
                    bruteForce(block_num + 1)
                    paper = deleteBlock(j, i, blocks[block_num][2], paper)


bruteForce(0)
if len(answer_arr) == 0:
    print("gg")

else:
    answer_arr.sort(key=lambda x: "".join(x))
    for i in range(L):
        print(answer_arr[0][i])
