# 1399 보물의 위치
import sys

T = int(sys.stdin.readline())

dig_dp = {}


def dig(x):  # dig 함수를 dp를 활용해 구현
    if x in dig_dp:
        return dig_dp[x]
    if x < 10:
        dig_dp[x] = x
        return x
    else:
        val = 0
        for c in str(x):
            val += int(c)
        dig_dp[x] = dig(val)
        return dig_dp[x]


def get_cor(
    arr, dir
):  # 현재방향이 주어졌을 때,(방향은 북,동,남,서를 0,1,2,3이라고 지정) 주어진 arr값만큼 방향을 바꿔가며 이동, 최종 좌표를 반환
    x, y = 0, 0
    arr_v = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i = dir
    for num in arr:
        x += num * arr_v[i % 4][0]
        y += num * arr_v[i % 4][1]
        i += 1
    return (x, y)


for _ in range(T):
    K, M = list(map(int, sys.stdin.readline().split()))
    if K == 1:  # start보다 K가 작을 때의 예외처리
        print(0, 1)
        continue
    arr = []
    golden_num = 1
    for i in range(10):  # loop의 최대크기가 9이므로, 10번 반복하며 loop를 탐색
        val = dig(golden_num)
        if val not in arr:
            arr.append(val)
            golden_num = val * M
        else:
            arr.append(val)
            break
    start = arr.index(arr[-1])
    start_x, start_y = get_cor(
        arr[:start], 0
    )  # loop를 찾았을 때, loop가 시작하기 이전까지 이동한 위치를 start x,y라고 하자
    arr = arr[start:-1]
    unit_x, unit_y = get_cor(arr * 4, start)  # 하나의 loop가 돌아가며 움직이는 좌표를 loop의 갯수만큼 곱해준다.
    unit_x *= (K - start) // (len(arr) * 4)
    unit_y *= (K - start) // (len(arr) * 4)
    remain_x, remain_y = get_cor(
        (arr * 4)[: ((K - start) % (len(arr) * 4))], start
    )  # 모듈러 연산을 통해 남아있는 움직임을 연산
    unit_x += remain_x
    unit_y += remain_y
    print(unit_x + start_x, unit_y + start_y)
