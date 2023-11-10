# 1506 경찰서
import sys
import itertools
from collections import deque

N = int(sys.stdin.readline())
cost_arr = list(map(int, sys.stdin.readline().split()))
board = [[0] * N for _ in range(N)]
group = [[] for _ in range(N)]
for i in range(N):  # input data로부터 graph 구성
    line = sys.stdin.readline()
    for j in range(N):
        if line[j] == "1":
            group[i].append(j)
for i in range(N):  # 시작점 i로부터 j까지 도달이 가능한지를 확인, 이를 통한 2차원 배열을 구성
    visited = [0] * N
    deq = deque([i])
    while deq:
        curr = deq.pop()
        if visited[curr] == 0:
            visited[curr] = 1
            for c in group[curr]:
                if visited[c] == 0:
                    deq.append(c)
    for j in range(N):
        if visited[j] == 1:
            board[i][j] = 1


arr = [i for i in range(N)]
for c in itertools.combinations(
    range(N), 2
):  # node a와 b가 상호 이동이 가능할 때, b의 parent를 a로 설정
    if (board[c[0]][c[1]] == 1) & (board[c[1]][c[0]] == 1):
        arr[c[1]] = c[0]
group = []
for i in range(N):  # arr를 거슬러 올라가면서 node간의 grouping
    flag = False
    for g in group:
        if arr[i] in g:
            g.append(i)
            flag = True
    if flag == False:
        group.append([i])
ans = 0
for g in group:  # group 내에서 가장 적은 cost를 가진 node만을 선택, 결과값을 도출
    g_cost = [cost_arr[i] for i in g]
    ans += min(g_cost)
print(ans)
