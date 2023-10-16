import sys
import itertools

L, N = list(map(int, sys.stdin.readline().split()))
puzzles = list(map(int, sys.stdin.readline().split()))
if puzzles[0] > L:
    print(0)
    exit()
puzzles.sort(reverse=True)

# puzzles_sum = sum(puzzles)
# for i in range(N):
#     minimum = puzzles_sum
#     maximum = 0
#     for iter in itertools.combinations(range(N), i):
#         min_idx = 0
#         sum = 0
#         for it in iter:
#             if it == min_idx:
#                 min_idx += 1
#             sum += puzzles[it]
#         minimum = min(minimum, sum)
#         maximum = max(maximum, sum + (1 + i) * puzzles[min_idx] - 1)
#     if (L >= minimum) & (L <= maximum):
#         print(i)
#         exit()
dic = {}


def expo_to_num(expo):
    count = 0
    while expo > 1:
        count += 1
        expo /= 2
    return count


def get_range(num):
    if num in dic:
        return dic[num]
    if num == 0:
        return -1
    first_idx = expo_to_num(num & (-num))
    prev_range = get_range(num & (num - 1))
    if prev_range == -1:
        minimum_idx = N - 1 if first_idx != N - 1 else N - 2
        minimum = puzzles[first_idx]
        maximum = puzzles[first_idx] + 2 * puzzles[minimum_idx] - 1
        dic[num] = (minimum, maximum, minimum_idx, 1)
        return (minimum, maximum, minimum_idx, 1)
    else:
        if prev_range[2] == first_idx:
            minimum = prev_range[0] + puzzles[first_idx]
            maximum = (
                prev_range[0]
                + puzzles[first_idx]
                + (2 + prev_range[3]) * puzzles[first_idx - 1]
                - 1
            )
            dic[num] = (minimum, maximum, first_idx - 1, prev_range[3] + 1)
            return (minimum, maximum, first_idx - 1, prev_range[3] + 1)
        else:
            minimum = prev_range[0] + puzzles[first_idx]
            maximum = prev_range[1] + puzzles[first_idx] + puzzles[prev_range[2]]
            dic[num] = (minimum, maximum, prev_range[2], prev_range[3] + 1)
            return (minimum, maximum, prev_range[2], prev_range[3] + 1)


value = N
for i in range((1 << N) - 1):
    value_range = get_range(i)
    if value_range != -1:
        if (L >= value_range[0]) & (L <= value_range[1]):
            value = min(value, value_range[3])

print(value)
