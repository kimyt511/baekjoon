# 1473 미로탈출
import sys
from collections import deque
N, M = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
    board.append(sys.stdin.readline()[:-1])

def arr_to_num(arr): # array를 arr에서 C의 위치를 표현하는 비트마스크로 변환
    num = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'C':
                num |= 1<<(i*M+j)
    return num

def num_to_arr(num): # 비트마스크에서 array로 변환, 변환 중 원본 board를 참고해 A와 B는 유지
    _board = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (board[i][j] == 'A') | (board[i][j] == 'B'):
                _board[i][j] = board[i][j]
            else:
                if num & (1<<(i*M+j)):
                    _board[i][j] = 'C'
                else:
                    _board[i][j] = 'D'
    return _board

def turn_room(arr, x, y): # 현재 좌표가 x,y인 상황에서 방의 회전 발생시에 변경된 arr 반환
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 'C') | (arr[i][j] == 'D'):
                if i == y:
                    arr[i][j] = 'C' if arr[i][j]=='D' else 'D'
                if j == x:
                    arr[i][j] = 'C' if arr[i][j]=='D' else 'D'
    return arr
def check_range(x,y):
    return (x in range(M)) & (y in range(N))
deq = deque([(0,0,0, arr_to_num(board))]) # 현재 좌표 x,y,걸린시간,board 상황
dp = {}
while deq:
    x,y,time, num_arr = deq.pop()
    if (x==M-1)&(y==N-1): # 도착점 도착시에 걸린 시간 출력
        print(time)
        exit()
    if (x,y,num_arr) not in dp: # BFS를 통해 구현하기에 가장 먼저 x,y,num_arr에 도착한 경우가 가장 빠른 경우이다.
        dp[(x,y,num_arr)] = time
        arr = num_to_arr(num_arr)
        for v in [(1,0),(-1,0)]: # 좌우로 움직이는 경우
            if check_range(x+v[0], y+v[1]):
                if (arr[y][x] == 'A') | (arr[y][x] == 'D'):
                    if (arr[y+v[1]][x+v[0]] == 'A') | (arr[y+v[1]][x+v[0]] == 'D'):
                        deq.appendleft((x+v[0], y+v[1], time+1, num_arr))
        for v in [(0,1),(0,-1)]: # 상하로 움직이는 경우
            if check_range(x+v[0], y+v[1]):
                if (arr[y][x] == 'A') | (arr[y][x] == 'C'):
                    if (arr[y+v[1]][x+v[0]] == 'A') | (arr[y+v[1]][x+v[0]] == 'C'):
                        deq.appendleft((x+v[0], y+v[1], time+1, num_arr))
        
        turn_arr = turn_room(num_to_arr(num_arr),x,y) # 방을 회전하는 경우
        deq.appendleft((x,y,time+1,arr_to_num(turn_arr)))

print(-1) # 도착점까지 도달하지 못할 때는 -1을 출력
