#1234 크리스마스 트리
import sys
from collections import deque
import math
arr = list(map(int, sys.stdin.readline().split()))

def numberOfCase(num):
    case = []
    if num%1==0:
        case.append((num,0,0))
        case.append((0,num,0))
        case.append((0,0,num))
    if num%2 == 0:
        _num = int(num/2)
        case.append((_num,_num,0))
        case.append((_num,0,_num))
        case.append((0,_num,_num))
    if num%3 == 0:
        _num = int(num/3)
        case.append((_num,_num,_num))
    return case

deq = deque()
dic = {}
deq.append((1,arr[1],arr[2],arr[3],1))
answer = 0
while deq:
    level, r, g, b, curr = deq.pop()
    if level > arr[0]:
        answer = answer + curr
    else:
        for case in numberOfCase(level):
            if (r >= case[0]) & (g >= case[1]) & (b>=case[2]):
                multi = int(math.factorial(level) / math.factorial(case[0]) / math.factorial(case[1]) / math.factorial(case[2]))
                deq.append((level+1, r-case[0], g-case[1], b-case[2], curr*multi))

print(answer)