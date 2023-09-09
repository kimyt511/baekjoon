import sys
from collections import deque

def weightToMin(w):
    sum = w // 40
    for i in range(4,1,-1):
        w = w % (10*i)
        sum = sum + w // (10*(i-1))
    return sum

N = int(sys.stdin.readline())
input_data = sys.stdin.readline().split()
input_data.append("20")
weight = 20
stack = deque()
sum_weight = 0
sum_count = 0
for w in input_data:
    curr_w = int(w) - weight
    sum_weight = sum_weight + abs(curr_w)
    if curr_w > 0:
        stack.append(curr_w)
    elif curr_w < 0:
        while(curr_w < 0):
            pop_w = stack.pop()
            if (pop_w + curr_w) < 0:
                sum_count = sum_count + weightToMin(pop_w)
            else:
                sum_count = sum_count + weightToMin(abs(curr_w))
            curr_w = pop_w + curr_w
        if curr_w > 0:
            stack.append(curr_w)
    weight = int(w)

print(sum_weight, sum_count*4)

