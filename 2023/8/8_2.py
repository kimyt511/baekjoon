import sys

N = int(sys.stdin.readline())
answer = [0] * N
inputValue = list(map(int, sys.stdin.readline().split()))
input_num = inputValue.pop()
stack = [(input_num, N - 1)]
length = 0
for idx in range(N - 2, -1, -1):
    input_num = inputValue.pop()
    while stack[length][0] <= input_num:
        num, seq = stack.pop()
        answer[seq] = idx + 1
        length = length - 1
        if length < 0:
            break
    stack.append((input_num, idx))
    length = length + 1


for ans in answer:
    print(ans, end=" ")
