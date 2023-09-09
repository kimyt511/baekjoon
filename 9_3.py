import sys
import itertools
import math

T = int(sys.stdin.readline())


def VectorMatching():
    N = int(sys.stdin.readline())
    pos_arr = []
    for _ in range(N):
        pos_arr.append(list(map(int, sys.stdin.readline().split())))
    minimum = sys.maxsize
    for minus_idx in itertools.combinations(range(N), int(N / 2)):
        pos_x = 0
        pos_y = 0
        for idx in range(N):
            if idx in minus_idx:
                pos_x = pos_x - pos_arr[idx][0]
                pos_y = pos_y - pos_arr[idx][1]
            else:
                pos_x = pos_x + pos_arr[idx][0]
                pos_y = pos_y + pos_arr[idx][1]
        minimum = min(minimum, math.sqrt(pos_x**2 + pos_y**2))
    print(minimum)


for _ in range(T):
    VectorMatching()
