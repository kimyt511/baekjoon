# 1385 벌집
import sys
from collections import deque

a, b = list(map(int, sys.stdin.readline().split()))
cor_arr = [0] * 1001000  # 숫자를 좌표로 바꿔주는 배열
cor_board = [[0] * 1500 for _ in range(1500)]  # 좌표를 숫자로 바꿔주는 배열
# 각 배열의 크기는 어림잡아 적당한 크기로 설정
cor_arr[1] = (750, 750)  # 1번을 750, 750으로 설정
i = 2
curr_x, curr_y = 750, 750
group_num = 1
while i <= max(a, b):  # 벌집 배열 생성
    curr_x -= 1
    curr_y += 1
    for v in [
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
    ]:  # 8가지 방향 중 6개를 골라 해당 방향으로만 움직일 수 있도록 설정
        for j in range(group_num):
            curr_x += v[0]
            curr_y += v[1]
            cor_arr[i] = (curr_x, curr_y)
            cor_board[curr_x][curr_y] = i
            i += 1
    group_num += 1

deq = deque([(a, -1)])
visited = [0] * 1001000
route = [
    0
] * 1001000  # 특정 노드로 접근하는 경우는 한가지 밖에 없으므로, 해당 경우 이전 노드를 기록, 역추적을 통해 경로를 찾을 수 있도록 함
while deq:  # bfs를 통해 탐색
    curr, prev = deque.popleft(deq)
    if curr == b:
        route[curr] = prev
        arr = []
        while curr != -1:
            arr.append(curr)
            curr = route[curr]
        arr.reverse()
        print(*arr)
        exit()
    if (visited[curr] == 0) & (cor_arr[curr] != 0):
        visited[curr] = 1
        route[curr] = prev
        curr_x, curr_y = cor_arr[curr]
        for v in [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]:
            next = cor_board[curr_x + v[0]][curr_y + v[1]]
            if visited[next] == 0:
                deq.append((next, curr))
