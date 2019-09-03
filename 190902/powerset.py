"""
# powerset with binary numbers
a = [1,2,3]
N = 3
for i in range(2**N):
    for j in range(N):
        print(bin(i), bin(1 << j))
        if i & (1 << j):
            print(a[j], end='')
    print()
"""

# powerset with dfs
N = 5
idx = [i for i in range(N)]

res = []
def dfs(depth, case):
    if depth == N:
        res.append(case)
        return
    for i in range(2):
        if i:
            case.append(depth)
            dfs(depth+1, [*case])
            case.pop()
        else:
            dfs(depth+1, [*case])

dfs(0,[])

print(res, len(res))