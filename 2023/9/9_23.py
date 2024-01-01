import sys

R, C = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(R):
    arr.append(sys.stdin.readline()[:-1])

check_dia = [[[] for _ in range(C)] for _ in range(R)]


def check_arr_value(x, y):
    if (x in range(0, R)) & (y in range(0, C)):
        return arr[x][y]
    else:
        return -1


answer = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "1":
            check_dia[i][j].append((1, 0))
            if check_arr_value(i - 1, j + 1) == "1":
                for dia in check_dia[i - 1][j + 1]:
                    if (dia[1] == 0) & (check_arr_value(i, j + 2 * dia[0]) == "1"):
                        check_dia[i][j].append((dia[0] + 1, 0))
            if check_arr_value(i - 1, j - 1) == "1":
                for dia in check_dia[i - 1][j - 1]:
                    if ((dia[0] - dia[1]) != 1) & (
                        check_arr_value(i, j + 2 * (dia[0] - dia[1] - 2)) == "1"
                    ):
                        check_dia[i][j].append((dia[0], dia[1] + 1))
                        if dia[0] == dia[1] + 2:
                            answer = max(answer, dia[0])

print(answer)
