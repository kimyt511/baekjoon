import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
table = []
for i in range(N):
    table.append(sys.stdin.readline())

answer = 0
dic = [[[] for _ in range(N)] for _ in range(10)]


def ownersToNum(arr):
    sum = 0
    for i in range(N):
        if arr[i] == 1:
            sum = sum + 2**i
    return sum


def dfs(credit, owner, owners, length):
    global answer
    if length > answer:
        answer = length
    dic[credit][owner].append(owners)
    for i in range(N):
        if (int(table[owner][i]) >= credit) & ((owners & (1 << i)) == 0):
            _owners = owners | (1 << i)
            if _owners not in dic[int(table[owner][i])][i]:
                dfs(int(table[owner][i]), i, _owners, length + 1)


dfs(0, 0, 1, 1)

print(answer)
