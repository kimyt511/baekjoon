import sys
from queue import Queue

N = int(sys.stdin.readline())
stack = []
order = 0
operation = Queue()
for i in range(1, N + 1):
    num = int(sys.stdin.readline())
    if num >= order:
        while num != order:
            order = order + 1
            stack.append(order)
            operation.put("+")
        stack.pop()
        operation.put("-")
    elif num < order:
        pop_num = stack.pop()
        if pop_num == num:
            operation.put("-")
        else:
            print("NO")
            exit()

while not operation.empty():
    print(operation.get())
