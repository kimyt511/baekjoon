# 1133 반복되지 않는 단어

import sys

K, N, A = list(map(int, sys.stdin.readline().split()))
alphabet_arr = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
][:A]


def checkString(string):
    if len(string) == 1:
        return True
    length = len(string)
    for i in range(1, int(length / K) + 1):
        arr = []
        for j in range(i):
            arr.append(string[length - j - 1])
        flag = False
        for j in range(K):
            for l in range(i):
                # print(arr, j, l)
                if arr[l] != string[length - i * j - l - 1]:
                    flag = True
        if flag == False:
            return False
    return True


def addString(string):
    if len(string) == N:
        print(string)
        exit()
    for c in alphabet_arr:
        if checkString(string + c):
            addString(string + c)


addString("")
print(-1)
