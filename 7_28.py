import itertools


def sorting(l, k, idx):
    return l[0:idx] + l[idx : idx + k][::-1] + l[idx + k : int(N)]


N, K = input().split()
arr = list(map(int, input().split()))
answer_list = sorted(arr)
permut = {l: -1 for l in itertools.permutations(answer_list, int(N))}
stack = [(arr, 0)]
answer = -1

if arr == answer_list:
    answer = 0
    stack = []

while len(stack) != 0:
    arr, count = stack.pop(0)
    for i in range(int(N) - int(K) + 1):
        sorted_arr = sorting(arr, int(K), i)
        if sorted_arr == answer_list:
            answer = count + 1
            stack = []
            break
        elif permut[tuple(sorted_arr)] == -1:
            permut[tuple(sorted_arr)] = count + 1
            stack.append((sorted_arr, count + 1))


print(answer)
