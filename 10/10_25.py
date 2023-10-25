# 1177 조쌤포스
import sys
import math
import heapq

N, R, Bx, By, Bvx, Bvy = list(map(int, sys.stdin.readline().split()))
R = R + 0.0001  # 문제에서 제시한 오차범위
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

range_arr = []
# 근의 공식을 사용, 이차부등식의 해를 통해 i번째 학생과 조쌤의 거리가 R 이하인 t의 범위를 구함
for i in arr:
    a, b, c, d = Bvx - i[2], Bx - i[0], Bvy - i[3], By - i[1]
    A, B, C = a * a + c * c, a * b + c * d, b * b + d * d - R * R
    if ((B * B - A * C) >= 0) & (A != 0):
        route_val = math.sqrt(B * B - A * C)
        min_t, max_t = (-B - route_val) / A, (-B + route_val) / A
        if A > 0:
            if max_t >= 0:  # range normalize
                range_arr.append((max(min_t, 0), max_t))
        else:
            if min_t >= 0:
                range_arr.append((0, min_t))
            range_arr.append((max(0, max_t), sys.maxsize))
    elif A == 0:  # 2차항의 상수가 0일 떄는, 일차부등식의 해를 이용해 범위를 구함
        if (B == 0) & (C <= 0):
            range_arr.append((0, sys.maxsize))
        elif B != 0:
            value = -C / B
            if value >= 0:
                range_arr.append((0, value))


range_arr.sort()
heap = []
curr = 0
ans = 0
for i in range_arr:  # 범위 정렬 후, heap에 pop과 push를 반복해 범위 안에 있는 학생의 수를 구함
    while heap:  # len(heap)이 아닌 curr 변수를 쓴 이유는 시간의 효율성을 위함 O(n^2) -> O(n)
        if heap[0] < i[0]:
            heapq.heappop(heap)
            curr -= 1
        else:
            break
    heapq.heappush(heap, i[1])
    curr += 1
    ans = max(ans, curr)

print(ans)
