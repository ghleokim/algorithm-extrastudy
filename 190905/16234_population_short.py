"""
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
import sys
sys.setrecursionlimit(10**6)
e,f=(1,-1,0,0),(0,0,1,-1)
def d(i,j):
    for k in range(4):
        p,q=i+e[k],j+f[k]
        if any((p<0,q<0,p>N-1,q>N-1)):continue
        D=abs(B[p][q]-B[i][j])
        if L<=D<=R and not V[p][q]:V[p][q]=1;a.append((p,q));d(p,q)
def s(i,j):
    global M,a
    if V[i][j]:return
    a=[(i,j)];V[i][j]=1;d(i,j);L=len(a)
    if L==1:return
    M,S=1,sum(B[i][j]for i,j in a)
    for i,j in a:B[i][j]=S//L
N,L,R=map(int,input().split())
B,C,M=[[*map(int,input().split())]for l in range(N)],0,1
while M:
    M,V=0,[[0]*N for l in range(N)]
    [s(i,j)for i in range(N)for j in range(N)]
    C+=1 if M else 0
print(C)


"""
2 20 50
30 30
30 50

"""