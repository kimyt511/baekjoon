from collections import deque
import sys

M, T, N = list(map(int, sys.stdin.readline().split()))
answer = [0] * N
arr = []
left = deque()
right = deque()
time = 0
boat = 0  # 0이 left, 1이 right

for i in range(N):
    t, pos = sys.stdin.readline().split()
    t = int(t)
    arr.append((t, pos, i))
arr.sort(key=lambda x: x[0])

for i in range(N):
    t, pos, idx = arr[i]
    if pos == "left":
        left.append((t, idx))
    else:
        right.append((t, idx))
lenL = len(left)
lenR = len(right)


def checkTime(len, boat, time):
    if len == 0:
        return False
    if boat == 0:
        return left[0][0] <= time
    else:
        return right[0][0] <= time


def checkNext():
    if lenL == 0:
        return (right[0][0], 1)
    elif lenR == 0:
        return (left[0][0], 0)
    else:
        if left[0][0] == right[0][0]:
            return (left[0][0], boat)
        elif left[0][0] < right[0][0]:
            return (left[0][0], 0)
        else:
            return (right[0][0], 1)


while (lenL != 0) | (lenR != 0):
    if boat == 0:
        if checkTime(lenL, boat, time):
            for _ in range(M):
                if lenL == 0:
                    break
                elif left[0][0] <= time:
                    _, idx = left.popleft()
                    lenL = lenL - 1
                    answer[idx] = time + T
                else:
                    break
            boat = 1 - boat
            time = time + T
        else:
            next_t, next_pos = checkNext()
            if time <= next_t:
                if next_pos == boat:
                    time = next_t
                else:
                    boat = 1 - boat
                    time = next_t + T
            else:
                if next_pos == boat:
                    time = time
                else:
                    boat = 1 - boat
                    time = time + T
    else:
        if checkTime(lenR, boat, time):
            for _ in range(M):
                if lenR == 0:
                    break
                elif right[0][0] <= time:
                    _, idx = right.popleft()
                    lenR = lenR - 1
                    answer[idx] = time + T
                else:
                    break
            boat = 1 - boat
            time = time + T
        else:
            next_t, next_pos = checkNext()
            if time <= next_t:
                if next_pos == boat:
                    time = next_t
                else:
                    boat = 1 - boat
                    time = next_t + T
            else:
                if next_pos == boat:
                    time = time
                else:
                    boat = 1 - boat
                    time = time + T

for i in range(N):
    print(answer[i])
