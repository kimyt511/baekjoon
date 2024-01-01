#1047 울타리
import sys
from collections import deque
N = int(sys.stdin.readline())
trees = []
for _ in range(N):
    trees.append(list(map(int, sys.stdin.readline().split())))

dic = {}
deq = deque()
deq.append(((1<<N) - 1, 0, 0))
while deq:
    arr, num, count = deq.popleft()
    if arr not in dic:
        dic[arr] = 1
        minx, miny, maxx, maxy, num_max = sys.maxsize, sys.maxsize, 0,0,0
        for i in range(N):
            if(arr & (1<<i)):
                if trees[i][0] < minx:
                    minx = trees[i][0]
                    minx_idx = i
                if trees[i][1] < miny:
                    miny = trees[i][1]
                    miny_idx = i
                if trees[i][0] > maxx:
                    maxx = trees[i][0]
                    maxx_idx = i
                if trees[i][1] > maxy:
                    maxy = trees[i][1]
                    maxy_idx = i
                if trees[i][2] > num_max:
                    num_max = trees[i][2]
                    num_idx = i
        if (maxx-minx + maxy - miny)*2 <= num:
            print(count)
            exit()
        else:
            for i in [minx_idx, miny_idx, maxx_idx, maxy_idx, num_idx]:
                if(arr & (1<<i)):
                    if (arr & ~(1<<i)) not in dic:
                        deq.append((arr & ~(1<<i), num+trees[i][2], count+1))
