# 1782 거울 숫자
import sys

A, B = list(map(int, sys.stdin.readline().split()))
dic = {"0": "0", "1": "1", "2": "5", "8": "8", "5": "2"}


def make_digit_even(num):  # 주어진 수로 짝수 길이의 디지털 숫자 반환
    arr = list(str(num))
    _arr = [dic[arr[i]] for i in range(len(arr) - 1, -1, -1)]
    return int("".join(arr + _arr))


def make_digit_odd(num):  # 주어진 수로 홀수 길이의 디지털 숫자 반환
    arr = list(str(num))
    _arr = [dic[arr[i]] for i in range(len(arr) - 1, -1, -1)]
    return int("".join(arr + _arr[1:]))


ans = 0  # 모든 경우의 수를 확인, 조건에 맞는 수가 나올 때마다 ans + 1
for a in ["0", "1", "2", "5", "8"]:
    for b in ["0", "1", "2", "5", "8"]:
        for c in ["0", "1", "2", "5", "8"]:
            for d in ["0", "1", "2", "5", "8"]:
                for e in ["0", "1", "2", "5", "8"]:
                    for f in ["0", "1", "2", "5", "8"]:
                        for g in ["0", "1", "2", "5", "8"]:
                            for h in ["0", "1", "2", "5", "8"]:
                                for i in ["0", "1", "2", "5", "8"]:
                                    num = int(a + b + c + d + e + f + g + h + i)
                                    even = make_digit_even(num)
                                    if even in range(A, B + 1):
                                        ans += 1
                                        print(even)
                                    if i in ["0", "1", "8"]:
                                        odd = make_digit_odd(num)
                                        if odd in range(A, B + 1):
                                            ans += 1
                                            print(odd)
if 0 in range(A, B + 1):  # 0의 경우, 2번 더해지기 때문에 예외 처리
    ans -= 1
print(ans)
