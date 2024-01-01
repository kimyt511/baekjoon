# 1786 찾기
# KMP 알고리즘

import sys

T = sys.stdin.readline()[:-1]
P = sys.stdin.readline()[:-1]
len_T, len_P = len(T), len(P)

Pi = [0] * len_P  # 접두사와 접미사가 일치하는 최대 접두사의 길이
j = 0
for i in range(1, len_P):
    while (j > 0) & (P[i] != P[j]):
        j = Pi[j - 1]
    if P[i] == P[j]:
        Pi[i] = j + 1
        j += 1

ans = []
j = 0
for i in range(len_T):  # O(N)의 시간동안, 일치하지 않는 상황에서 T의 바로 다음 char와 가능한 먼 P의 char를 비교
    while (j > 0) & (T[i] != P[j]):
        j = Pi[j - 1]
    if T[i] == P[j]:
        if j == len_P - 1:
            ans.append(i - len_P + 2)
            j = Pi[j]
        else:
            j += 1

print(len(ans))
print(*ans)
