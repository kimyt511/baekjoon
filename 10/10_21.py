# 1087 쥐 잡기
import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))


def get_time_to_value(t):
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for i in range(N):
        _x = data[i][0] + t * data[i][2]
        _y = data[i][1] + t * data[i][3]
        min_x, max_x = min(min_x, _x), max(max_x, _x)
        min_y, max_y = min(min_y, _y), max(max_y, _y)
    return max(max_x - min_x, max_y - min_y)


p = 0
q = 2000
for i in range(100):
    a = (2 * p + q) / 3
    b = (p + 2 * q) / 3
    if get_time_to_value(a) < get_time_to_value(b):
        q = b
    else:
        p = a
    if p >= q:
        break
print(get_time_to_value(p))
