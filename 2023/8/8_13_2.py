import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
one_side = ((N - 2) ** 2) * 5 + (N - 2) * 4
two_side = (N - 1) * 4 + (N - 2) * 4
three_side = 4
two_min = min(
    [
        num[0] + num[1],
        num[0] + num[2],
        num[0] + num[3],
        num[0] + num[4],
        num[1] + num[2],
        num[1] + num[3],
        num[1] + num[5],
        num[2] + num[4],
        num[2] + num[5],
        num[3] + num[4],
        num[3] + num[5],
        num[4] + num[5],
    ]
)
three_min = min(
    [
        num[0] + num[1] + num[2],
        num[0] + num[2] + num[4],
        num[0] + num[3] + num[4],
        num[0] + num[1] + num[3],
        num[5] + num[1] + num[2],
        num[5] + num[2] + num[4],
        num[5] + num[3] + num[4],
        num[5] + num[1] + num[3],
    ]
)
if N == 1:
    print(sum(num) - max(num))
else:
    print(one_side * min(num) + two_side * two_min + three_side * three_min)
