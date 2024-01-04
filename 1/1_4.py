# 1300 K번째 수
# 특정 숫자를 바탕으로 모든 열을 탐색하며 특정 숫자가 몇번째 수인지를 확인, target과 비교하며 이분탐색 진행
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

start = 1
end = N * N
result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for div in range(1, N + 1):
        cnt += min(mid // div, N)
    if cnt >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
