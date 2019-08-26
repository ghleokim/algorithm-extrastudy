# https://www.acmicpc.net/problem/2636
from pprint import pprint
"""
0 공기중인 상태 판별
1 가장자리 탐색(녹을 치즈 판별)
2 

5 5
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0

13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
"""

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append([*map(int, input().split())])
pprint(board)

melt = [[0 for _ in range(M)] for __ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]

#ESWN
dr = (0,1,0,-1)
dc = (1,0,-1,0)

def checkBoundary(r,c):
    if any((r<0,c<0,r==N,c==M)):return False
    return True

def checkAir():
    # dfs를 이용한 완전탐색
    i,j = 0,0
    
    stack = [0] * 10000
    
    stack[0] = (i,j)
    top = 0

    while top != -1:
        r,c = stack[top]
        stack[top] = 0
        top -= 1
        board[r][c] = 8

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if checkBoundary(nr,nc):
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if not board[nr][nc] or board[nr][nc] == 8:
                        top += 1
                        stack[top] = (nr,nc)


def seek(i,j):
    # dfs를 이용한 완전탐색
    # 만약 4 사이드가 모두 치즈라면 melt = 0
    # 만약 4 사이드 중 하나라도 공기라면 melt = 1
    # visited는 두 경우 모두 체크
    stack = [0] * 10000
    visited[i][j] = 1
    stack[0] = (i,j)
    top = 0
    
    while top != -1: # block을 전부 탐색할 때까지
        r,c = stack[top]
        stack[top] = 0
        top -= 1

        air=False
        for k in range(4):
            nr,nc = r+dr[k], c+dc[k]
            if board[nr][nc] == 1:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    top += 1
                    stack[top] = (nr,nc)
            elif board[nr][nc] == 8:
                air = True
        if air:
            melt[r][c] = 1
    

hr = 0
newcnt = 0


while True:
    newcnt = 0
    visited = [[0 for _ in range(M)] for __ in range(N)]
    checkAir()
    visited = [[0 for _ in range(M)] for __ in range(N)]
    finished = True
    for i in range(1,N-1):
        for j in range(1,M-1):
            if board[i][j] == 1:
                finished = False
                if not visited[i][j]:
                    seek(i,j)
    if finished:
        break
    for i in range(1,N-1):
        for j in range(1,M-1):
            if board[i][j] == 1:
                newcnt += 1
            if melt[i][j]:
                board[i][j] = 8

    for i in range(N):
        print(melt[i], board[i])
    print(newcnt)    

    hr += 1
    cnt = newcnt

print(hr, cnt)

pprint(board)

# while True:
#     visited = [[0 for _ in range(M)] for __ in range(M)]
#     finished = True
#     newcnt = 0
#     for i in range(1,N-1):
#         for j in range(1,M-1):
#             if board[i][j] == 1:
#                 finished = False
#                 if not visited[i][j]:
#                     newcnt+=1
#                     seek(i,j)

#     if finished:
#         break
    
#     for i in range(1,N-1):
#         for j in range(1,M-1):
#             if melt[i][j]:
#                 board[i][j] = 8
#     hr += 1
#     cnt = newcnt

# print(hr + 1)
# print(cnt)