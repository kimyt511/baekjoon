import sys
import itertools

N = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))


def isitPrime(k):  # k가 소수인지 판별
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k**0.5) + 1, 2):
        if k % i == 0:
            return False

    return True


max_ans = -1
min_ans = sys.maxsize
for permutation in itertools.permutations(range(N), N):  # 가능한 모든 배열을 확인
    dp = {}

    def addOperation(x, y):  # index가 x부터 y까지인 범위에서 나올 수 있는 모든 수 반환
        global num_arr
        if (x, y) in dp:
            return dp[(x, y)]
        if x == y:
            return [num_arr[permutation[x]]]
        arr = []
        dic = {}
        for k in range(x, y):
            arr1 = addOperation(x, k)
            arr2 = addOperation(k + 1, y)
            for i in arr1:
                for j in arr2:
                    if i + j not in dic:
                        dic[i + j] = 1
                        arr.append(i + j)
                    if i * j not in dic:
                        dic[i + j] = 1
                        arr.append(i * j)
                    if i - j not in dic:
                        dic[i + j] = 1
                        arr.append(abs(i - j))
                    if j != 0:
                        if i // j not in dic:
                            dic[i // j] = 1
                            arr.append(i // j)
                    if i != 0:
                        if j // i not in dic:
                            dic[j // i] = 1
                            arr.append(j // i)
        dp[(x, y)] = arr
        return arr

    curr_arr = addOperation(0, N - 1)
    for c in curr_arr:  # max_ans, min_ans 갱신
        if isitPrime(c):
            max_ans = max(c, max_ans)
            min_ans = min(c, min_ans)

if max_ans == -1:
    print(-1)
else:
    print(min_ans)
    print(max_ans)
