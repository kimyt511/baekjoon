# 1311 할 일 정하기
# 할 일을 정할 사람(idx)와, 남은 할일 (bitmask)로 dp
import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dic = {}


def get_min(idx, bitmask):
    if (idx, bitmask) in dic:
        return dic[(idx, bitmask)]
    if idx < 0:
        return 0
    ans = sys.maxsize
    for i in range(N):
        if bitmask & (1 << i):
            _bitmask = bitmask & (~(1 << i))
            value = board[idx][i] + get_min(idx - 1, _bitmask)
            ans = min(ans, value)
    dic[(idx, bitmask)] = ans
    return ans


print(get_min(N - 1, (1 << N) - 1))
