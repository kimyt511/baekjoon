# 1409 점 칠하기
import sys
import itertools

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

diff_arr = [[] for _ in range(360)]  # 두 점간의 각차이를 기록
for c in itertools.combinations(arr, 2):
    diff_arr[c[1] - c[0]].append((c[0], c[1]))
    diff_arr[360 + c[0] - c[1]].append((c[1], c[0]))
ans = 0
for arr in diff_arr:
    _arr = [i for i in arr]
    count = 0
    visited = [0] * 360
    while (
        _arr
    ):  # 해당 간격에 해당하는 점들의 집합에 대해, 겹쳐있는 경우에는 양 끝 점이 포함된 set을 포함시키고, 끝점이 없는 경우에는 아무 set 하나를 포함시키며 칠할 점들을 고른다.
        count_arr = [0] * 360
        for c in _arr:
            count_arr[c[0]] += 1
            count_arr[c[1]] += 1
        if count_arr.count(1) == 0:
            count += 1
            visited[_arr[0][0]] = 1
            visited[_arr[0][1]] = 1
            _arr = _arr[1:]
        else:
            next_arr = []
            for c in _arr:
                if (count_arr[c[0]] == 1) | (count_arr[c[1]] == 1):
                    if (visited[c[0]] == 0) & (visited[c[1]] == 0):
                        count += 1
                        visited[c[0]] = 1
                        visited[c[1]] = 1
                else:
                    next_arr.append(c)
            _arr = next_arr
    ans = max(ans, count)

print(ans * 2)  # ans는 set의 개수이므로, 칠한 점의 개수는 2배
