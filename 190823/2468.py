# https://www.acmicpc.net/problem/2468

"""
N * N 이차원배열,
"""
"""
N = int(input())

board = [[] for _ in range(5)]

for i in range(N):
    board[i] = [*map(int, input().split())]

print(board)
"""

direction = [(0, 1), (1, 0), (0,-1), (-1, 0)]


def checkWall(x, y, di):
    nx = x + direction[di][0]
    ny = y + direction[di][1]
    if any((nx == 0, nx > N, ny == 0, ny > N)):
        return False
    else:
        return True


def safeUpdate(x, y, k):
    if board[x][y] < k:
        safe[x][y] = 1


def bfs(x, y):
    global visited
    global safe

    queue = []

    queue.append((x, y))

    while queue:
        xi, yi = queue[0][0], queue[0][1]
        del queue[0]
        for n in range(4):
            if checkWall(xi, yi, n):
                nx, ny = xi + direction[n][0], yi + direction[n][1]
                if board[nx][ny] and not visited[nx][ny] and safe[nx][ny]:
                    queue.append((nx, ny))

        visited[xi][yi] = 1

    return 1


N = int(input())

board = [[0 for _ in range(N+2)] for __ in range(N+2)]

max_height = 0

for x in range(1,N+1):
    temp = [*map(int, input().split())]
    for y in range(1, N+1):
        board[x][y] = temp[y-1]
        if temp[y-1] > max_height:
            max_height = temp[y-1]

safe = [[0 for _ in range(N+2)] for __ in range(N+2)]

max_result = 0

for k in range(max_height, 0, -1):

    visited = [[0 for _ in range(N+2)] for __ in range(N+2)]
    result = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            safeUpdate(i, j, k)
            if board[i][j] and not visited[i][j]:
                result += bfs(i, j)

    if result > max_result:
        result = max_result

print(max_result)

