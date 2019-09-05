# 인접리스트
from pprint import pprint

di=(1,-1,0,0)
dj=(0,0,1,-1)

# def checkBorder(i,j):
#     for k in range(4):
#         ni,nj = i+di[k], j+dj[k]
#         if any((ni<0, nj<0, ni>N-1, nj>N-1)):
#             continue
#         diff = abs(board[ni][nj]-board[i][j])
#         if L <= diff <= R:
#             border[i][j].append((ni,nj))

def seekboard(i,j):
    allies = [(i,j)]
    visited[i][j] = 1

    stack = [(i,j)]

    while stack:
        ci,cj = stack[0]
        del stack[0]
        # visited[ci][cj] = 1

        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if any((ni<0, nj<0, ni>N-1, nj>N-1)):
                continue
            diff = abs(board[ni][nj] - board[ci][cj])
            if diff >= L and diff <= R and not visited[ni][nj]:
                visited[ni][nj]=1
                stack.append((ni,nj))
                allies.append((ni,nj))
    
    return allies
        
    
N,L,R = map(int,input().split())
board = [[*map(int,input().split())] for __ in range(N)]
# border = [[0 for _ in range(N)] for __ in range(N)]

# print(border)

# for i in range(N):
#     for j in range(N):
#         checkBorder(i,j)

count = 0
moved = True

while moved:
    moved = False
    visited = [[0 for _ in range(N)] for __ in range(N)]
    for r in board: print(r)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                allies = seekboard(i,j)
                print(i,j,allies)
                numAllies = len(allies)

                if numAllies == 1:
                    continue

                moved = True
                sumAllies = sum([board[i][j] for i,j in allies])
                for x,y in allies:
                    board[x][y] = sumAllies // numAllies
    if moved: count += 1

print(count)

"""
2 20 50
30 30
30 50
"""