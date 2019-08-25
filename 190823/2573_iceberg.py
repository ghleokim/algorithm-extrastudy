# https://www.acmicpc.net/problem/2573


"""
빙산이 녹아 두 덩어리 이상으로 분리되는 최초의 시간 구하기
다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력

배열의 첫번째, 마지막 행 / 열에는 0이 들어간다.
    == boundary check not needed

N, M
for i in range(1, N-1)
    for j in range(1, M-1)
        board[i][j]
로 호출

board가 전부 0인지 판별하는 bool - 해가 지나갈 때마다 False로 재설정
    board를 전부 탐색했음에도 false라면 0을 출력

탐색 중 하나라도 존재한다면 True로 설정, 이후 탐색

test case
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0


5 7
0 0 0 0 0 0 0
0 1 100 30 1 0 0
0 1 0 20 100 1 0
0 1 100 30 1 0 0
0 0 0 0 0 0 0

"""

from pprint import pprint

d = ((0, 1), (1, 0), (0, -1), (-1, 0)) # East South West North

# BFS
def checkIce(x, y):
    global board
    global melt
    global visited

    queue = [(x, y)]
    visited[x][y] = 1

    while queue:
        print(queue)
        (xi, yi) = queue[0]
        del queue[0]

        for di in range(4):
            nx, ny = xi + d[di][0], yi + d[di][1]
            if board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
            elif not board[nx][ny]:
                melt[xi][yi] += 1

# N, M = 5, 7
N, M = map(int, input().split())

board = [[0 for _ in range(M)] for __ in range(N)]
melt = [[0 for _ in range(M)] for __ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]

input()
for r in range(1,N-1):
    temp = [*map(int, input().split())]
    for c in range(1,M-1):
        board[r][c] = temp[c]
input()


year = 0
ice = True

while ice:
    melt = [[0 for _ in range(M)] for __ in range(N)]
    visited = [[0 for _ in range(M)] for __ in range(N)]
    count = 0
    ice = False
    for i in range(1, N-1):
        for j in range(1, M-1):
            if board[i][j]:
                ice = True
                if not visited[i][j]:
                    count += 1
                    checkIce(i, j) # check visited for all icebergs near
    
    for i in range(1, N-1):
        for j in range(1, M-1):
            if melt[i][j]:
                m = board[i][j] - melt[i][j]
                if m < 0:
                    board[i][j] = 0
                else:
                    board[i][j] = m
    
    
    print('board')
    pprint(board)
    
    if count == 1:
        year += 1
        continue
    elif count > 1:
        ice = False
        print(year)
    else:
        ice = False
        print(0)