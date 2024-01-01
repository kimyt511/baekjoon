import sys
from collections import deque

N, M, L = list(map(int, sys.stdin.readline().split()))
string = sys.stdin.readline()
len_string = len(string) - 1
position_dictionary = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    position_dictionary[i] = []
board = []
for i in range(N):
    line = sys.stdin.readline()
    for j in range(M):
        position_dictionary[line[j]].append((i, j))
    board.append(line)

dp = {}


def check_reachable(x, y, i, j):
    v_x, v_y = abs(x - i), abs(y - j)
    return (v_x + v_y > 4) & (min(v_x, v_y) > 1)


def get_count(x, y, idx):
    if (x, y, idx) in dp:
        return dp[(x, y, idx)]
    if idx == len_string - 1:
        return 1
    count = 0
    for i in position_dictionary[string[idx + 1]]:
        if check_reachable(x, y, i[0], i[1]):
            count += get_count(i[0], i[1], idx + 1)
            if count > 1000000007:
                count -= 1000000007
    dp[(x, y, idx)] = count
    return count


answer = 0
for i in position_dictionary[string[0]]:
    answer += get_count(i[0], i[1], 0)
    if answer > 1000000007:
        answer -= 1000000007

print(answer)
