# 1095 마법의 구슬
import sys
import math

S, F, M = list(map(int, sys.stdin.readline().split()))
arr = [0] * (M + 1)
prime_dic = {}
prime_arr = []
for i in range(2, M + 1):
    if arr[i] == 0:
        prime_dic[i] = 0
        prime_arr.append(i)
        for j in range(2 * i, M + 1, i):
            arr[j] = 1


def prime_factorization(num, r, vec):
    curr = r
    while curr <= num:
        prime_dic[r] += int(num / curr) * vec
        curr *= r


def check(num):
    curr = num
    for i in range(len(prime_arr)):
        count = 0
        while curr % prime_arr[i] == 0:
            count += 1
            curr = int(curr / prime_arr[i])
        if count > prime_dic[prime_arr[i]]:
            return False
    return True


for p in prime_arr:
    prime_factorization(S + F, p, 1)
    prime_factorization(F, p, -1)
    prime_factorization(S, p, -1)

for i in range(M, 0, -1):
    if check(i):
        print(i)
        exit()
print(-1)
