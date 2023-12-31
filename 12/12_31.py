# 1230 문자열 거리
# i와 j가 같을 때와 다를 때, 해당 j를 채용할지 말지를 대상을 2개의 dp를 유지
import sys

O = sys.stdin.readline()[:-1]
N = sys.stdin.readline()[:-1]
len_O = len(O)
len_N = len(N)


dic = {}
for i in range(-1, len_O):  # 불가능하다면 가능한 최대값보다 큰 1000을 넣는다
    dic[(i, 0)] = 1000
    dic[(i, 1)] = 1000
dic[(-1, 0)] = 0  # 빈 문자열이 빈 문자열이 되기 위한 문자열의 수
for j in range(len_N):
    next_dic = {(-1, 0): 1000, (-1, 1): 1}  # 빈 문자열이 하나의 문자가 되기 위해서는 하나의 문자열이 필요

    for i in range(len_O):
        if O[i] == N[j]:
            next_dic[(i, 0)] = min(
                dic[(i - 1, 0)], dic[(i - 1, 1)]
            )  # 둘이 같다면, 해당 채용할 때, 그 이전 dp의 최소값과 같다
        else:
            next_dic[(i, 0)] = 1000  # 둘이 다르다면, 채용 불가능
        next_dic[(i, 1)] = min(
            dic[(i, 0)] + 1, dic[(i, 1)]
        )  # 채용하지 않을 것이라면, 이전 채용할 때보다 문자열이 하나 늘거나, 아예 채용하지 않았을 때와 같다
    dic = next_dic

ans = min(dic[(len_O - 1, 0)], dic[(len_O - 1, 1)])
if ans == 1000:
    print(-1)
else:
    print(ans)
