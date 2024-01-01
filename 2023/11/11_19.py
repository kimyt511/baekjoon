# 1559 놀라운 미로
# python 시간 초과
import sys
from collections import deque

while True:
    M, N = list(map(int, sys.stdin.readline().split()))
    if M + N == 0:
        exit()
    door_arr = []
    for _ in range(M):
        door_arr.append(sys.stdin.readline()[:-1])
    K = int(sys.stdin.readline())
    box_cors = []
    for _ in range(K):
        x, y = list(map(int, sys.stdin.readline().split()))
        box_cors.append((x - 1, y - 1))
    direction_dic = {"N": 0, "E": 1, "S": 2, "W": 3}
    vector_dic = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def get_door(x, y, t):
        curr = door_arr[x][y]
        return (direction_dic[curr] + t) % 4

    def check_range(x, y):
        return (x in range(M)) & (y in range(N))

    deq = deque([(0, 0, 0, 0)])
    dp = [[[[0] * 4 for _ in range(1 << K)] for _ in range(N)] for _ in range(M)]

    while deq:
        cur_x, cur_y, time, cur_box = deq.popleft()
        # print(cur_x, cur_y, time, cur_box)
        if (cur_box == ((1 << K) - 1)) & (cur_x == M - 1) & (cur_y == N - 1):
            print(time)
            break
        else:
            if dp[cur_x][cur_y][cur_box][time % 4] == 0:
                dp[cur_x][cur_y][cur_box][time % 4] = 1
                deq.append((cur_x, cur_y, time + 1, cur_box))
                curr_vec = vector_dic[get_door(cur_x, cur_y, time)]
                if check_range(cur_x + curr_vec[0], cur_y + curr_vec[1]):
                    for i in range(K):
                        if box_cors[i] == (cur_x + curr_vec[0], cur_y + curr_vec[1]):
                            cur_box |= 1 << i
                    deq.append(
                        (cur_x + curr_vec[0], cur_y + curr_vec[1], time + 1, cur_box)
                    )
