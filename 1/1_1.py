# 1242 소풍
import sys

N, K, M = list(map(int, sys.stdin.readline().split()))
curr = M  # 현재 target의 idx만 바꿔가면서, 몇 번째 cycle에 아웃되는지를 확인
ans = 0
while N != ans:
    target = K % (N - ans)  # 이번에 잘릴 idx
    if target == 0:
        target = N - ans
    if curr == target:
        ans += 1
        break
    if curr > target:  # 잘릴 idx의 위치에 따라, target의 idx를 변경
        curr = curr - target
    else:
        curr += N - ans - target
    ans += 1
print(ans)
