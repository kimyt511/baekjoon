# 1529 동민 수열
import sys

N, L = list(map(int, sys.stdin.readline().split()))
numbers = sys.stdin.readline()[:-1].split()
arr = [[[] for _ in range(2)] for _ in range(2)]
for (
    num_str
) in numbers:  # 주어진 배열의 수가 금민수라면, 시작하는 문자와 끝나는 문자가 4인지 7인지를 구분, 중복될 수를 고려해 arr에 저장
    isGoldenNum = True
    for c in num_str:
        if (c != "4") & (c != "7"):
            isGoldenNum = False
    if isGoldenNum:
        start = 0 if num_str[0] == "4" else 1
        end = 0 if num_str[len(num_str) - 1] == "4" else 1
        if num_str not in arr[start][end]:
            arr[start][end].append(num_str)

count_arr = [[0] * 2 for _ in range(2)]  # arr에 저장된 수를 통해 시작과 끝나는 문자에 대해 count_arr를 구성
for i in range(2):
    for j in range(2):
        count_arr[i][j] = len(arr[i][j])

dp = {}


def dongmin_arr(num, start, end):  # logN의 시간복잡도로 구하기 위해, 절반으로 나눠가며 계산
    if num == 1:
        return count_arr[start][end]
    if (num, start, end) in dp:
        return dp[(num, start, end)]
    val = 0
    next_num = num // 2
    if num % 2 == 0:
        for i in range(2):
            val += dongmin_arr(next_num, start, i) * dongmin_arr(next_num, i, end)
    else:
        for i in range(2):
            for j in range(2):
                val += (
                    dongmin_arr(next_num, start, i)
                    * dongmin_arr(next_num, i, j)
                    * count_arr[j][end]
                )
    if val > 1234567891:
        val %= 1234567891
    dp[(num, start, end)] = val
    return val


ans = 0
for i in range(2):
    for j in range(2):
        ans += dongmin_arr(L, i, j)
if ans > 1234567891:
    ans %= 1234567891
print(ans)
