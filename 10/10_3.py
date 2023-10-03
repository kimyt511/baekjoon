# 1102 발전소
import sys
import heapq

N = int(sys.stdin.readline())
cost_arr = []
for _ in range(N):
    cost_arr.append(list(map(int, sys.stdin.readline().split())))
line = sys.stdin.readline()
count = 0
bit = 0
for i in range(N):
    if line[i] == "Y":
        bit += 1 << i
        count += 1
P = int(sys.stdin.readline())
if P > N:
    print(-1)
    exit()
heap = []
dic = {}
heapq.heappush(heap, (0, bit, count))
while heap:
    cost, bit, count = heapq.heappop(heap)
    if bit not in dic:
        dic[bit] = 1
        if count >= P:
            print(cost)
            exit()
        for i in range(N):
            if bit & (1 << i):
                for j in range(N):
                    if (bit & (1 << j)) == False:
                        _bit = bit | (1 << j)
                        if _bit not in dic:
                            heapq.heappush(
                                heap, (cost + cost_arr[i][j], _bit, count + 1)
                            )

print(-1)
