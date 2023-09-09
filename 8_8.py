import sys
from collections import deque
N = int(sys.stdin.readline())

six_number_arr = []
six_number = 1
six_gap = 1

while six_number <= N:
    six_number_arr.append(six_number)
    six_gap = six_gap + 4
    six_number = six_number + six_gap
if N > 146858:
    possible = 3
elif N > 1791:
    possible = 4
else:
    possible = 6
minimum_arr = [0]*N
que = deque([N])
dic = {N:0}
while len(que) != 0:
    num = que.pop()
    minimum = dic[num]
    for i in six_number_arr:
        next_num = num - i
        if (num - i < 0) | (minimum >= possible):
            continue
        elif num - i == 0:
            print(minimum+1)
            exit()
        else:
            que.appendleft(num-i)
            if num-i in dic:
                dic[num-i] = min(dic[num-i], minimum+1)
            else:
                dic[num-i] = minimum+1
