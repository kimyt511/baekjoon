# 1139 울타리
import sys
import itertools
import math
from collections import deque
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)
deq = deque()
deq.append((0,1<<N, N))
dic = {}
def get_maximum(num):
    if num in dic:
        return dic[num]
    _arr = []
    for i in range(N):
        if num & (1<<i):
            _arr.append(i)
    maximum = 0
    for i in itertools.combinations(_arr,3):
        if arr[i[1]] + arr[i[2]] > arr[i[0]]:
            _num = ((num & ~(1 << i[0])) & ~(1 << i[1])) & ~(1 << i[2])
            p = (arr[i[0]]+arr[i[1]]+arr[i[2]])/2
            value = math.sqrt(p*(p-arr[i[0]])*(p-arr[i[1]])*(p-arr[i[2]]))
            maximum = max(maximum, get_maximum(_num)+value)
    dic[num] = maximum
    return maximum
    
print(get_maximum((1<<N)-1))


    

