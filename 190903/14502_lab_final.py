# https://www.acmicpc.net/submit/14502/14953203

def check0(board):
    res = []
    for i in range(N):
        for j in range(M):
            if not board[i][j]: res.append((i,j))
    
    return res


def check0num(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not board[i][j]: cnt += 1
    
    return cnt


def spread(board, case):
    dx = (1,-1,0,0)
    dy = (0,0,-1,1)
    # deep copy board
    newboard = [[*board[i]] for i in range(N)]
    for c in case:
        newboard[c[0]][c[1]] = 1

    visited = [[0 for _ in range(M)] for __ in range(N)]

    for i in range(N):
        for j in range(M):
            if newboard[i][j] == 2 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = 1
                while stack:
                    ci,cj = stack.pop()
                    for k in range(4):
                        ni, nj = ci + dx[k], cj + dy[k]
                        if any((ni < 0, nj < 0, ni > N-1, nj > M-1)): continue
                        if newboard[ni][nj] == 2 and not visited[ni][nj]:
                            stack.append((ni,nj))
                            visited[ni][nj] = 1
                        elif newboard[ni][nj] == 0 and not visited[ni][nj]:
                            newboard[ni][nj] = 2
                            visited[ni][nj] = 1
                            stack.append((ni,nj))    
    return newboard


def makeCase(n, s=0, case=[]):
    if len(case) == 3:
        yield case
    else:
        for i in range(s, n):
            case.append(i)
            yield from makeCase(n, i+1, [*case])
            case.pop()

            
N, M = map(int,input().split())

max_safe = 0
candi = []
cases = []

board = [[*map(int,input().split())] for _ in range(N)]

# 보드의 0 후보군 설정
candi = check0(board)
# print(len(candi))

for case in makeCase(len(candi)):
    newboard = spread(board, [candi[c] for c in case])
    res = check0num(newboard)
    if max_safe < res:
        max_safe = res

print(max_safe)