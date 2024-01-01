import sys

N, M = list(map(int, sys.stdin.readline().split()))

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end, length = list(map(int, sys.stdin.readline().split()))
    tree[start].append((end, length))
    tree[end].append((start, length))


def search(prev, curr, end, length):
    for node in tree[curr]:
        if node[0] != prev:
            if node[0] == end:
                print(length + node[1])
            else:
                search(curr, node[0], end, length + node[1])


for _ in range(M):
    start, end = list(map(int, sys.stdin.readline().split()))
    search(0, start, end, 0)
