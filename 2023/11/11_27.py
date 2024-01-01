# 1653 양팔 저울
# 전체를 브루드포스하지 않고, 가능한 무게 별로 브루드포스를 진행
import sys
import itertools

N = int(sys.stdin.readline())
pendulum_arr = list(map(int, sys.stdin.readline().split()))
pendulum_arr.sort()
K = int(sys.stdin.readline())

weight_arr = [[] for _ in range(120)]
for i in range(98766):  # 무게 별로 추의 배치를 저장
    visited = [1] * 10
    string = str(i)
    string = "0" * (5 - len(string)) + string
    for s in string:
        if s != "0":
            visited[int(s)] -= 1
    if all([True if s >= 0 else False for s in visited]):
        val = 0
        for j in range(len(string)):
            val += int(string[-1 - j]) * (j + 1)
        weight_arr[val].append(string)
possible_arr = [0]

for weight in weight_arr:  # 무게별로 저장된 추의 배치가 주어진 추를 이용해 배치 가능한지 확인
    for c in itertools.combinations(weight, 2):
        visited = [0] * 10
        for pen in pendulum_arr:
            visited[pen] = 1
        for i in c[0] + c[1]:
            if i != "0":
                visited[int(i)] -= 1
        if all([True if i >= 0 else False for i in visited]):
            possible_arr.append(int(c[0] + c[1][::-1]))
            possible_arr.append(int(c[1] + c[0][::-1]))

possible_arr.sort()  # 가능한 배치들을 정렬 후, 적절한 값을 출력
if len(possible_arr) <= K:
    print(possible_arr[-1])
else:
    print(possible_arr[K])
