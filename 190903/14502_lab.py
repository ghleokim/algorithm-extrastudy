# https://www.acmicpc.net/problem/14502
# 연구소

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
    # pprint(newboard)
    for c in case:
        newboard[c[0]][c[1]] = 1
    # pprint(newboard)
    #print(newboard, id(newboard), id(board))

    visited = [[0 for _ in range(M)] for __ in range(N)]

    for i in range(N):
        for j in range(M):
            if newboard[i][j] == 2 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = 1
                while stack:
                    # print(stack)
                    ci,cj = stack.pop()
                    # if not visited[ci][cj]:
                    #     visited[ci][cj] = 1
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
                # pprint(newboard)
    
    return newboard

# def makeCase(n, case=[]):
#     if len(case) == 3:
#         cases.append([*case])
#         return
#     else:
#         for i in range(n):
#             print(i,end='')
#             if not visited[i]:
#                 case.append(i)
#                 print(case)
#                 visited[i] = 1
#                 makeCase(n, [*case])
#                 case.pop()
#                 makeCase(n, [*case])

def makeCase(n, s=0, case=[]):
    if len(case) == 3:
        yield case
        # cases.append(case)
        # return
    else:
        for i in range(s, n):
            # if not visited[i]:
            case.append(i)
            yield from makeCase(n, i+1, [*case])
            case.pop()
        
            

"""
def makeCase(n):
    for i in range(2**n):
        # print(i, end = '')
        c = []
        found= False
        for j in range(n):
            # print(bin(1 << j))
            if i & (1 << j):
                if len(c) == 3:
                    found = True
                    break
                c.append(j)
        if found:
            continue
        if len(c) == 3:
            print(c)
            cases.append(c)
"""
        
            

from pprint import pprint

N, M = map(int,input().split())

max_safe = 0
candi = []
cases = []

board = [[*map(int,input().split())] for _ in range(N)]

# pprint(board)
# print(check0(board,[(0,1),(0,2),(0,3)]))

# 보드의 0 후보군 설정
candi = check0(board)
# print(len(candi))

for case in makeCase(len(candi)):
    newboard = spread(board, [candi[c] for c in case])
    # print([candi[c] for c in case], end = ' ')
    res = check0num(newboard)
    if max_safe < res:
        max_safe = res

print(max_safe)






