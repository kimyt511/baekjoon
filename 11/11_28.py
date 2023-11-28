# 1704 붕어빵타이쿤
import sys

M, N = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))
ans_arr = []
ans_min = sys.maxsize
for i in range(
    1 << N
):  # 첫 줄을 브루드포스로 고정, 첫줄이 정해지면 다음줄은 자동으로 정해지기 때문에, 마지막 줄이 조건에 맞는지 확인
    line_arr = [i]
    for y in range(M - 1):
        next = 0
        for x in range(N):
            node = 0
            for cor in [(x, y), (x + 1, y), (x - 1, y), (x, y - 1)]:
                if (cor[0] in range(N)) & (cor[1] in range(M)):
                    if line_arr[cor[1]] & (1 << cor[0]):
                        node ^= 1
            if board[y][x] != node:
                next |= 1 << x
        line_arr.append(next)
    y = M - 1
    flag = True
    for x in range(N):
        node = 0
        for cor in [(x, y), (x + 1, y), (x - 1, y), (x, y - 1)]:
            if (cor[0] in range(N)) & (cor[1] in range(M)):
                if line_arr[cor[1]] & (1 << cor[0]):
                    node ^= 1
        if board[y][x] != node:
            flag = False
    if flag:  # 1의 개수를 세어, 1의 개수가 최소인 배열들 만을 저장
        count = 0
        arr = ["0"] * M * N
        for x in range(N):
            for y in range(M):
                if line_arr[y] & (1 << x):
                    arr[y * N + x] = "1"
                    count += 1
        if ans_min == count:
            ans_arr.append("".join(arr))
        elif ans_min > count:
            ans_min = count
            ans_arr = ["".join(arr)]
if ans_arr:  # 조건에 맞게 출력
    ans_arr.sort()
    for i in range(M):
        print(" ".join(ans_arr[0][i * N : i * N + N]))
else:
    print("IMPOSSIBLE")
