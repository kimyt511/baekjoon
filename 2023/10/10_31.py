#1306 달려라 홍준

import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
tree = {}

def make_tree(start, end): # tree 생성, binary 구간별로 최대값을 저장하는 tree
    if (start, end) in tree:
        return tree[(start, end)]
    elif start == end:
        tree[(start,end)] = arr[start]
        return arr[start]
    else:
        middle = (start+end)//2
        value = max(make_tree(start, middle), make_tree(middle+1, end))
        tree[(start, end)] = value
        return value

make_tree(0,N-1)

def search_tree(start, end, left, right): # 최대값을 구해야하는 구간을 binary 구간으로 쪼개며 tree에서 탐색해, 결국 해당 구간에서의 최대값을 return
    if (left > end) | (right < start):
        return 0
    elif (left <= start) & (right >= end):
        return tree[(start, end)]
    else:
        middle = (start + end) // 2
        return max(search_tree(start, middle, left, right), search_tree(middle+1, end, left, right))
    
ans = []
for i in range(M-1, N-M+1):
    ans.append(search_tree(0, N-1, i-M+1, i+M-1))

print(*ans)