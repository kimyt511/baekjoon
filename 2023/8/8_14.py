import sys

N, M = list(map(int, sys.stdin.readline().split()))
boxes = [0] * (M + 1)
for _ in range(N):
    box = list(map(int, sys.stdin.readline().split()))
    if box.count(0) < (M - 1):
        boxes[0] = boxes[0] + 1
    else:
        for i in range(M):
            if box[i] != 0:
                boxes[i + 1] = boxes[i + 1] + 1
count = sum([x - 1 if x != 0 else x for x in boxes])
if boxes[0] != 0:
    print(count)
elif count > 0:
    print(count - 1)
else:
    print(count)
