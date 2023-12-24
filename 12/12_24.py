# 1981 배열에서 이동
# 이분탐색을 활용, start부터 end까지 범위로 board에서 이동 가능한 경로가 있는지를 확인
import sys
from collections import deque

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def check_range(x, y):
    return (x >= 0) & (x < N) & (y >= 0) & (y < N)


def check_avaliable(start, end):  # start에서 end까지의 범위로 board에서 이동 가능한 경로가 있는지를 확인
    visited = [[0] * N for _ in range(N)]
    deq = deque([(0, 0)])
    if (board[0][0] < start) | (board[0][0] > end):
        return False
    while deq:
        curr = deq.pop()
        if (curr[0] == N - 1) & (curr[1] == N - 1):
            return True
        if visited[curr[0]][curr[1]] == 0:
            visited[curr[0]][curr[1]] = 1
            for v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if check_range(curr[0] + v[0], curr[1] + v[1]):
                    next_num = board[curr[0] + v[0]][curr[1] + v[1]]
                    if (next_num >= start) & (next_num <= end):
                        if visited[curr[0] + v[0]][curr[1] + v[1]] == 0:
                            deq.appendleft((curr[0] + v[0], curr[1] + v[1]))
    return False


min_num = min([min(i) for i in board])
max_num = max([max(i) for i in board])
ans = sys.maxsize
start, end = 0, max_num - min_num
while start <= end:  # 이분탐색을 진행
    mid = (start + end) // 2
    flag = False
    for i in range(min_num, max_num + 1):  # 시작값을 매번 바꿔줌
        if check_avaliable(i, i + mid):
            flag = True

    if flag:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans)
