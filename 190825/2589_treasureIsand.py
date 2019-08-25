# https://www.acmicpc.net/problem/2589
"""
50 * 50
두 지점을 잡고 거리를 계산하기에는 너무 많은 시간이 든다.
BFS로 depth를 구한 다음, 가장 깊은 depth를 리턴하도록 함.
"""

print(ord('L'), ord('W'))

dt = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(i, j):
    global visited
    global board

    queue = []
    depth = 0
    visited[i][j] = 1
    queue.append((i, j, depth))

    while queue:
        (x, y, d) = queue[0]
        depth = d
        del queue[0]
        for i in range(4):
            nx, ny = x + dt[i][0], y + dt[i][1]
            if not board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, d+1))

    return depth

N, M = map(int, input().split())

board = [[1 for _ in range(M+2)] for __ in range(N+2)]
visited = [[0 for _ in range(M+2)] for __ in range(N+2)]

for i in range(1, N+1):
    temp = input()
    for j in range(1, M+1):
        board[i][j] = ord(temp[j-1])-76

res = []
max_result = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if not board[i][j]:
            visited = [[0 for _ in range(M+2)] for __ in range(N+2)]
            r = bfs(i, j)
            if r > max_result:
                max_result = r

print(max_result)


# #---------------#

# dt=((0,1),(1,0),(0,-1),(-1,0))
# def b(i,j):
#     q,dp,vt[i][j]=[(i,j,0)],0,1
#     while q:
#         (x,y,d)=q[0]
#         dp=d
#         del q[0]
#         for i in range(4):
#             nx,ny=x+dt[i][0],y+dt[i][1]
#             if not bd[nx][ny] and not vt[nx][ny]:
#                 vt[nx][ny] = 1
#                 q.append((nx,ny,d+1))
#     return dp
# N,M=map(int,input().split())
# bd=[[1 for _ in range(M+2)] for __ in range(N+2)]
# vt=[[0 for _ in range(M+2)] for __ in range(N+2)]
# for i in range(1,N+1):
#     t=input()
#     for j in range(1,M+1):bd[i][j]=ord(t[j-1])-76
# m=0
# for i in range(1,N+1):
#     for j in range(1,M+1):
#         if not bd[i][j]:
#             vt=[[0 for _ in range(M+2)] for __ in range(N+2)]
#             r=b(i,j)
#             if r>m:m=r
# print(m)