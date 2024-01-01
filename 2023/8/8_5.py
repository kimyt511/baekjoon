import sys
from collections import deque


def stringToList(str):
    return str.split()
def listToString(arr):
    return " ".join(arr)

N = int(sys.stdin.readline())
inputData = []
memory_i = []
dic = {}
que = deque()

for i in range(N):
    Q = sys.stdin.readline()
    inputData.append(Q)
    if Q[0] == "t":
        memory_i.append(int(Q.split()[1])-1)

for i in range(N):
    if i in memory_i:
        dic[i] = listToString(que)
    Q = inputData[i].split()
    if Q[0] == "a":
        que.append(Q[1])
    elif Q[0] == "s":
        que.pop()
    else:
        que = deque(stringToList(dic[int(Q[1])-1]))

    length = len(que)
    if length == 0:
        print(-1)
    else:
        print(int(que[length-1]))