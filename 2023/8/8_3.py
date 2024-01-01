import sys
from queue import Queue

N, K = sys.stdin.readline().split()
name_len_arr = [0] * 30
que = Queue()
answer = 0
for _ in range(int(K)):
    name_len = len(sys.stdin.readline())
    que.put(name_len)
    name_len_arr[name_len] = name_len_arr[name_len] + 1

for _ in range(int(N) - int(K)):
    next_name_len = len(sys.stdin.readline())
    que.put(next_name_len)
    name_len_arr[next_name_len] = name_len_arr[next_name_len] + 1
    curr_name_len = que.get()
    name_len_arr[curr_name_len] = name_len_arr[curr_name_len] - 1

    answer = answer + name_len_arr[curr_name_len]

for _ in range(int(K)):
    curr_name_len = que.get()
    name_len_arr[curr_name_len] = name_len_arr[curr_name_len] - 1
    answer = answer + name_len_arr[curr_name_len]

print(answer)
