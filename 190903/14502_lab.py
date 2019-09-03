# https://www.acmicpc.net/problem/14502
# 연구소

def check0(board, case = []):
    res = []
    for i in range(N):
        for j in range(M):
            if not board[i][j] and (i,j) not in case: res.append((i,j))
    
    return res

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

def makeCase(n, case=[]):
    if len(case) == 3:
        cases.append([*case])
        return
    else:
        for i in range(n):
            if not visited[i]:
                case.append(i)
                visited[i] = 1
                makeCase(n, [*case])
                case.pop()
                makeCase(n, [*case])
                visited[i] = 0
               
            

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

max_safe = N*M
candi = []
cases = []

board = [[*map(int,input().split())] for _ in range(N)]

print(board)
# print(check0(board,[(0,1),(0,2),(0,3)]))

candi = check0(board)
visited = [0 for _ in range(len(candi))]
print(len(candi), candi)
newB = spread(board, [(4,1),(3,5),(0,3)])
print(len(check0(newB)))
makeCase(len(candi))
print(cases)

# for case in cases:
#     print([candi[c] for c in case])
#     tmpboard = spread(board, [candi[c] for c in case])
#     pprint(tmpboard)
#     print(len(check0(tmpboard)))
