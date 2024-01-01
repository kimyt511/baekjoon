import sys
from collections import deque

N = int(sys.stdin.readline())
properties = list(map(int, sys.stdin.readline().split()))
R = []
for _ in range(N):
    R.append(list(map(int, sys.stdin.readline().split())))
player = int(sys.stdin.readline())
deq = deque()
survivors = (1 << N) - 1
dp = {}
answer = 0
if N % 2 != 0:
    vote_victim = properties.index(max(properties))
    if vote_victim == player:
        print(0)
        exit(0)
    else:
        survivors = survivors & ~(1 << vote_victim)
        properties[vote_victim] = -sys.maxsize
deq.append((survivors, properties, 0))
while deq:
    survivors, properties, nights = deq.popleft()
    if (properties.index(max(properties)) == player) & (nights != 0):
        answer = max(answer, nights)
    elif survivors not in dp:
        dp[survivors] = 1
        if nights != 0:
            vote_victim = properties.index(max(properties))
            survivors = survivors & ~(1 << vote_victim)
            properties[vote_victim] = -sys.maxsize
        for i in range(N):
            if (i != player) & ((survivors & (1 << i)) != 0):
                if survivors & ~(1 << i) not in dp:
                    _properties = [j for j in properties]
                    _properties[i] = -sys.maxsize
                    for j in range(N):
                        _properties[j] = _properties[j] + R[i][j]
                    deq.appendleft((survivors & ~(1 << i), _properties, nights + 1))
                    # deq.append((survivors & ~(1 << i), _properties, nights + 1)) --> 이건 안됨
print(answer)

# 왜 dfs는 되고 bfs는 안되는가
