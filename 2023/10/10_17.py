# 1154 팀 편성
import sys

N = int(sys.stdin.readline())
graph = [[i] for i in range(N + 1)]
for i in range(N + 1):
    graph[i].sort()
while True:
    start, end = list(map(int, sys.stdin.readline().split()))
    if (start == -1) & (end == -1):
        break
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, N + 1):
    graph[i].sort()


def contains_arr(arr1, arr2):
    cur = 0
    for i in arr1:
        if arr2[cur] == i:
            cur += 1
            if cur == len(arr2):
                return True
    return False


def check_group(arr):
    for i in arr:
        if contains_arr(graph[i], arr) == False:
            return False
    return True


def check_two_group(arr1, arr2):
    for i in arr1:
        if contains_arr(graph[i], arr2) == False:
            return False
    return True


def toggle_arr(arr):
    cur = 0
    length = len(arr)
    _arr = []
    for i in range(1, N + 1):
        if cur < length:
            if arr[cur] == i:
                cur += 1
            else:
                _arr.append(i)
        else:
            _arr.append(i)
    return _arr


def add_arr(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    return list(set(arr))


team1 = []
team2 = []
cur = 0
for i in range(1, N + 1):
    toggle = toggle_arr(graph[i])
    if check_group(toggle) == False:
        print(-1)
        exit()
    if check_two_group(team1, toggle):
        team1 = add_arr(team1, toggle)
    elif check_two_group(team2, toggle):
        team2 = add_arr(team2, toggle)
for i in range(1, N + 1):
    if (i not in team1) & (i not in team2):
        team1.append(i)
team1.sort()
print(1)
team1.append(-1)
team2.append(-1)
if 1 in team1:
    print(" ".join(list(map(str, team1))))
    print(" ".join(list(map(str, team2))))
else:
    print(" ".join(list(map(str, team2))))
    print(" ".join(list(map(str, team1))))
