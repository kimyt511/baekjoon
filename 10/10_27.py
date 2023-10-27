# 1214 쿨한 물건 구매
import sys

D, P, Q = list(map(int, sys.stdin.readline().split()))
# a*P + b*Q에 대해서 a가 Q이상의 경우 (a-Q)*P + (b+P)*Q는 같은 수이므로 a를 0부터 Q까지 증가시키며 D보다 큰 수를 탐색한다.
min_val = P - D % P if D % P != 0 else 0  # Q를 사용하지 않고, P만을 사용하는 값을 초기 val로 설정한다.
curr = D + P
for i in range(Q):
    curr -= P
    if curr < 0:
        break
    val = Q - curr % Q if curr % Q != 0 else 0
    min_val = min(min_val, val)


print(D + min_val)
