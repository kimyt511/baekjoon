# 1908 곱셈 전개식
# nC1 + nC2 + ... + nCn = 2^n -1
# 1*nC1 + 2*nC2 + ... + n * nCn = n*2^(n-1)-n-1 임을 활용
import sys

divid = 10000
N = int(sys.stdin.readline())
if N==1:
    print(4)
    exit()
ans = (4*N-4) % divid

dic = {}
def multi(n):
    if n in dic:
        return dic[n]
    if n == 1:
        return 2
    if n%2 == 0:
        val = multi(n//2) * multi(n//2)
    else:
        val = multi(n//2) * multi(n//2) * 2
    dic[n] = val%divid
    return val % divid


def get_diff(n): # 1부터 n까지 숫자를 연결했을 때의 총 길이와 n의 차이를 구해 값을 보정
    val = 0
    if n < 10:
        return 0
    for i in range(1,10):
        if n <= int('9'*(i+1)):
            val += (n - int('9'*i)) * i
            return val
        val += int('9'+'0'*i) * i
        val %= divid
    return val


multi_val = multi(N-1)
ans += multi_val * 2
ans %= divid

val = 2 * N * multi_val
val %= divid

ans += val
ans %= divid

val = multi_val + 1
val %= divid

ans += get_diff(N) * val
ans %= divid

print(ans)