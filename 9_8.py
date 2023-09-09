import sys

N = int(sys.stdin.readline())
supervisor = list(map(int, sys.stdin.readline().split()))
child_arr = [[] for _ in range(N)]
for i in range(1,N):
    child_arr[supervisor[i]].append(i)
call_time = [0]*N
for i in range(N-1,-1,-1):
    child_call_time = sorted([call_time[j] for j in child_arr[i]], reverse=True)
    if child_call_time:
        call_time[i] = max([j+child_call_time[j]+1 for j in range(len(child_call_time))])

print(call_time[0])