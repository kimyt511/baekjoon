# 1819 불끄기
# 왼쪽부터 훑으며 왼쪽에 켜진 스위치를 최소화하고, 이후 오른쪽부터 훑으면서 스위치의 갯수를 최소로 유지

import sys

L, T = list(map(int, sys.stdin.readline().split()))
str_L = list(sys.stdin.readline()[:-1])
str_T = list(sys.stdin.readline()[:-1])
if str_T.count("1") == 0:
    print(0)
    exit()

cut_idx = str_T.index("1")
slot = str_T[cut_idx:]
switchs = str_L[cut_idx:]
curr = []
# print(switchs, slot)
for i in range(len(switchs) - len(slot) + 1):
    # print(i, switchs)
    if switchs[i] == "1":
        curr.append(i + cut_idx + 1)
        for j in range(len(slot)):
            switchs[i + j] = str(int(switchs[i + j]) ^ int(slot[j]))
# print(curr)
for i in range(T):
    if str_T[T - i - 1] == "1":
        tail_idx = i
        break
slot = str_T[: T - tail_idx]
switchs = str_L[:cut_idx] + switchs
switchs = switchs[: L - tail_idx]
min_val = switchs.count("1")
ans = [i for i in curr]

length_L = len(switchs)
length_T = len(slot)
# print(switchs, slot)
for i in range(len(switchs) - len(slot) + 1):
    if switchs[length_L - 1 - i] == "1":
        curr.append(length_L - i - length_T + 1)
        for j in range(length_T):
            switchs[length_L - 1 - i - j] = str(
                int(switchs[length_L - 1 - i - j]) ^ int(slot[length_T - 1 - j])
            )
        if min_val > switchs.count("1"):
            min_val = switchs.count("1")
            ans = [i for i in curr]
print(len(ans))
for i in ans:
    print(i)
