# 1725 히스토그램
import sys

N = int(sys.stdin.readline())
length_arr = [0]
for _ in range(N):
    length_arr.append(int(sys.stdin.readline()))
length_arr.append(0)
ans = 0
stack = [0]
length = 0
for i in range(1, N + 2):
    while stack:
        if length_arr[stack[length]] <= length_arr[i]:  # 들어오는 값이 항상 오름차순을 유지하도록 관리
            break

        top = stack.pop()
        length -= 1
        ans = max(
            ans, length_arr[top] * (i - stack[length] - 1)
        )  # 값이 나갈 때, 나가는 값부터, 들어오는 idx까지의 직사각형 넓이를 구해, ans를 업데이트
    stack.append(i)
    length += 1

print(ans)
