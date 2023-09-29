# 1097 마법의 문자열
import sys
import itertools

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline()[:-1])
K = int(sys.stdin.readline())
if len("".join(arr)) % K != 0:
    print(0)
    exit()
_arr = [0] * (int(len("".join(arr)) / K) + 1)
prime_arr = []
for i in range(2, int(len("".join(arr)) / K) + 1):
    if _arr[i] == 0:
        if int(len("".join(arr)) / K) % i == 0:
            prime_arr.append(i)
        for j in range(2 * i, int(len("".join(arr)) / K) + 1, i):
            _arr[j] = 1


def checkString(string, num):
    for i in range(int(len(string) / num)):
        curr = string[i]
        for j in range(num):
            if curr != string[int(len(string) / num) * j + i]:
                return False

    return True


def checkString2(string, num):
    if checkString(string, num) == False:
        return False
    for p in prime_arr:
        if checkString(string, num * p):
            return False
    return True


count = 0
for com in itertools.permutations(arr, N):
    string = "".join(com)
    if checkString2(string, K):
        count += 1

print(count)
