# 1979 극적인 곱셈
import sys

N, K = list(map(int, sys.stdin.readline().split()))
dic = {}


def get_next(nums):  # 다음 자리수 계산
    next_num = nums[0] * N + nums[1]
    return (next_num % 10, next_num // 10)


stack = [(K, 0), get_next((K, 0))]
while stack:
    curr = stack[-1]
    if curr == (K, 0):  # loop 완성 시 결과값 출력
        arr = stack[:-1][::-1]
        ans = ""
        for c in arr:
            ans += str(c[0])
        if ans[0] == "0":  # 첫자리가 0일 경우, 자연수가 성립하지 않으므로 불가능
            print(0)
            exit()
        else:
            print(ans)
            exit()
    if curr in dic:  # 첫 자리가 아닌 loop 생성 시, 불가능
        print(0)
        exit()
    dic[curr] = 1
    stack.append(get_next(curr))

print(0)
