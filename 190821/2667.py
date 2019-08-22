# https://www.acmicpc.net/problem/2667
"""
정사각형 모양의 지도.
집이 좌우, 아래위에 다른 집이 있는 경우 같은 단지로 정의한다.
-------------
필요한 자료형:
list[list]  N * N 입력받은 행렬
list[list]  N * N 방문행렬
list        각 단지별 집의 갯수
int         단지의 갯수
int         단지 탐색 시작한 위치


dfs단계:
? * 1 visited
? * 1 stack

백트래킹으로 접근
--------------
작성순서

1 작은 행렬로 시작. 한 개 단지에 대하여 완전탐색이 되는지 확인
2 지도 각 위치를 탐색하며 각각의 단지 탐색을 시작하도록

--------------
pseudocode
1-1 재귀

list[list] board = [][]
Stack s
int i           # row
int j           # column
int res
tuple v = (i,j) # position
list visited

def DFS(v):
    if i == 0
        if j == 0
            if board[i][j+1] # checkRight
                if not visited[i][j+1]
                    s += v
                    visit
                    res += 1
                    v <- (i, j+1)
                    DFS(v)
            elif board[i+1][j] # checkBelow
                if not visited[i+1][j]
                    s += v
                    visit
                    res += 1
                    v <- (i+1, j)
                    DFS(v)
        elif j == N-1
            # checkLeft
                push, visit, res
                DFS(next)
            # checkBelow
                push, visit, res
                DFS(next)
        else
            # checkRight
                push, visit, res
                DFS(next)
            # checkLeft
                push, visit, res
                DFS(next)
            # checkBelow
                push, visit, res
                DFS(next)

    elif i == N-1

    elif j == 0

    elif j == N-1

    else # not boundary
        # checkRight
        # checkLeft
        # checkBelow
        # checkUp

        else
            return res


"""

from pprint import pprint

directions = [
    (0, 1),  # 0 east
    (1, 0),  # 1 south
    (0, -1), # 2 west
    (-1, 0)  # 3 north
]

def DFS(v):
    global res
    i, j = v
    # check paths
    if i == 0:
        if j == 0: # east, south
            track = [0,1]
        elif j == N-1: # west, south
            track = [1,2]
        else: # east, west, south
            track = [0,1,2]
    elif i == N-1:
        if j == 0: # east, north
            track = [0,3]
        elif j == N-1: # west, north
            track = [2,3]
        else: # east, west, north
            track = [0,2,3]
    elif j == 0: # east, north, south
        track = [0,1,3]
    elif j == N-1: # west, north, south
        track = [1,2,3]
    else: # east, west, north, south
        track = [0,1,2,3]

    if not visited[i][j]:
        visited[i][j] = 1
        res += 1

    for t in track:
        vi = (v[0] + directions[t][0], v[1] + directions[t][1])
        if board[vi[0]][vi[1]]:
            if not visited[vi[0]][vi[1]]:
                DFS(vi)

    return res

N = int(input())
board = [[0 for j in range(N)] for i in range(N)]
visited = [[0 for j in range(N)] for i in range(N)]
s = []
result = []

for i in range(N):
    row = input()
    for n, r in enumerate(row):
        if ord(r) == 49:
            board[i][n] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        elif visited[i][j] == 1:
            continue
        else:
            res = 0
            s = [(i, j)]
            temp = DFS((i,j))
            if temp is not None:
                result.append(temp)

result = sorted(result)

print(len(result))
for r in result:
    print(r)


# print(DFS((2,0)))


"""
7
0110100
0110001
1000101
0000010
0100000
0100110
0101000
"""