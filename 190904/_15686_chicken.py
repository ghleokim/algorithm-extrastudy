# bfs
N, M = map(int, input().split())

# 집, 치킨집 위치 검색
house = []
chicken = []

board = []

for i in range(N):
    row = [*map(int, input().split())]
    board.append(row)
    for j in range(N):
        if row[j] == 1: house.append((i,j))
        elif row[j] == 2: chicken.append((i,j))

print(board)
print(chicken, house)


# 치킨집 중 m개 선택 부분집합
# def comb(m, n=0, case=[]):
#     if len(case) == m:
#         yield case
#     elif m == n:
#         yield 
#     else:
#         for i in range(len(chicken)):
#             case.append(i)
#             v[i] = 1
#             yield from comb(m,n+1,[*case])
#             # v[i] = 0
#             case.pop()
#             yield from comb(m,n+1,[*case])

# print([c for c in comb(3)])
# N = 3
# comb(3)

# combination 3
def comb(d=0,s=0): # depth, startindex, yield
    if d == M:
        if len(cs) == 3:
            yield [*cs]
    else:    
        for i in range(s,N):
            cs.append(i)
            yield from comb(d+1,s+1)
            cs.pop()
            yield from comb(d+1,s+1)

cs=[]
for c in comb():
    print(c)


# 치킨거리
def chickenDist(i,j, case=[]):
    di, dj = (-1,1,0,0), (0,0,-1,1)
    queue = [(i,j)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    while queue:
        ci, cj = queue[0]
        del queue[0]
        visited[ci][cj] = 1
        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if any((ni<0, nj<0, ni>N-1, nj>N-1)):continue
            elif board[ni][nj] == 2 and not case:
                return (abs(ni-i)+abs(nj-j))
            elif board[ni][nj] == 2 and (ni,nj) not in case:
                return (abs(ni-i)+abs(nj-j))
            elif board[ni][nj] == 0 and not visited[ni][nj]:
                queue.append((ni,nj))
            elif board[ni][nj] == 2 and (ni,nj) in case and not visited[ni][nj]:
                queue.append((ni,nj))
    
    return 0


min_res = N ** 3
cs=[]
for case in comb():
    choice = [chicken[c] for c in case]
    res = 0
    for h in house:
        t = chickenDist(*h,choice)
        print(t, end=' ')
        res += t
    if min_res > res:
        min_res = res

