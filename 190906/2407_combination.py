# return nCm

n,m = map(int,input().split())

r = 1
for i in range(n-m+1,n+1): r *= i
for j in range(2,m+1): r//=j

print(r)

# print([1 * i // j for i in range(n-m+1,n+1) for j in range(2,m+1)])