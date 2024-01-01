# 1858 기울기가 가장 큰 두 점
# 여러 점 중 기울기가 가장 큰 두점은 정렬했을 때 x좌표가 연속되어 있다
import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    data.append((x, y, i + 1))

cor_arr = sorted(data)
max_val = -sys.maxsize
arr = []
for i in range(N - 1):  # 정렬된 좌표들을 기준으로 가장 큰 기울기와, 그 때 작은 점의 좌표를 구한다
    gradient = abs(
        (cor_arr[i][1] - cor_arr[i + 1][1]) / (cor_arr[i][0] - cor_arr[i + 1][0])
    )
    min_idx = min(cor_arr[i][2], cor_arr[i + 1][2])
    max_idx = max(cor_arr[i][2], cor_arr[i + 1][2])
    if gradient > max_val:
        arr = [(min_idx, max_idx)]
        max_val = gradient
    elif gradient == max_val:
        arr.append((min_idx, max_idx))

arr.sort()
start_idx = arr[0][0]
for i in range(start_idx, N):  # 여러 점이 하나의 직선 상에 위치할 떄, 정렬된 순서와 입력받은 순서가 다를 수 있기 떄문에
    gradient = abs(  # 작은 점의 좌표를 활용, 입력받은 가장 작은 좌표의 쌍을 구한다.
        (data[start_idx - 1][1] - data[i][1]) / (data[start_idx - 1][0] - data[i][0])
    )
    if gradient == max_val:
        print(start_idx, i + 1)
        exit()
