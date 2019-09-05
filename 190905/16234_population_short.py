import sys
sys.setrecursionlimit(10**6)
di,dj=(1,-1,0,0),(0,0,1,-1)
def sd(i,j):
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if any((ni<0,nj<0,ni>N-1,nj>N-1)): continue
        D=abs(B[ni][nj]-B[i][j])
        if L<=D<=R and not V[ni][nj]:V[ni][nj]=1;ad.append((ni,nj));sd(ni,nj)
N,L,R=map(int,input().split())
B,C,M=[[*map(int,input().split())]for __ in range(N)],0,1
while M:
    M,V=0,[[0 for _ in range(N)]for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if V[i][j]:continue
            ad=[(i,j)];V[i][j]=1;sd(i,j)
            if len(ad)==1:continue
            M,sumA=1,sum([B[i][j] for i,j in ad])
            for x,y in ad:B[x][y]=sumA//len(ad)
    C+=1 if M else 0
print(C)


import sys
sys.setrecursionlimit(10**6)
di,dj=(1,-1,0,0),(0,0,1,-1)
def sd(i,j):
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if any((ni<0,nj<0,ni>N-1,nj>N-1)):continue
        D=abs(B[ni][nj]-B[i][j])
        if L<=D<=R and not V[ni][nj]:V[ni][nj]=1;ad.append((ni,nj));sd(ni,nj)
def sl(i,j):
    global ad,M
    if V[i][j]:return
    ad=[(i,j)];V[i][j]=1;sd(i,j)
    if len(ad)==1:return
    M,sumA=1,sum([B[i][j]for i,j in ad])
    for x,y in ad:B[x][y]=sumA//len(ad)
N,L,R=map(int,input().split())
B,C,M=[[*map(int,input().split())]for __ in range(N)],0,1
while M:
    M,V=0,[[0 for _ in range(N)]for __ in range(N)]
    [sl(i,j)for i in range(N)for j in range(N)]
    C+=1 if M else 0
print(C)


"""
2 20 50
30 30
30 50

"""