"""
t = [3,5,1,1,2,4,2]
p = [10,20,10,20,15,40,200]
case = [1,2,3]
"""

N = int(input())
t, p = [], []

for i in range(N):
    it, ip = map(int, input().split())
    t.append(it)
    p.append(ip)

max_res = 0
max_case = []

enum=0
power = []
# make case with dfs(recursive)
visited = [0 for _ in range(N)]

# make case with binary
power = []
for i in range(2**N):
    case = []
    for j in range(N):
        if i & (1 << j):
            case.append(j)
    power.append(case)

for case in power:
    print(case)
    res = True
    for i in range(0, len(case)-1):
        if case[i] + t[case[i]] > case[i+1]:
            res = False
            break
        elif case[i] + t[case[i]] > N:
            res = False
            break
    if case:
        if case[-1]+t[case[-1]] > N:
            res = False

    if res:
        result = 0
        for c in case:
            result += p[c]
        if max_res < result:
            max_res = result
            max_case = case
    else:
        continue

print(max_res)
