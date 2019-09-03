"""
t = [3,5,1,1,2,4,2]
p = [10,20,10,20,15,40,200]
case = [1,2,3]
"""
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
"""
# -------------------------- #

# review
# dfs with c

def solve(k):
    global ans
    if k == N:
        for i in range(N):
            if Si[i]:
                for j in range(i + 1, i + Ti[i]):
                    if j >= N or Si[j] : return

        tsum = 0
        for i in range(N):
            if Si[i]:
                tsum += Pi[i]
        if tsum > ans : ans = tsum

    else:
        Si[k] = 1
        solve(k + 1)
        Si[k] = 0
        solve(k + 1)

N = int(input())

Ti = [0] * N 
Pi = [0] * N
Si = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

ans = 0
solve(0)

print(ans)







# def solve(k, s):
#     global ans
#     if k == N:
#         ans = max(ans, s)
#         return

#     if(k + Ti[k] <= N):
#         solve(k + Ti[k], s + Pi[k])

#     solve(k + 1, s)

# N = int(input())

# Ti = [0] * N
# Pi = [0] * N

# for i in range(N):
#     Ti[i], Pi[i] = map(int, input().split())

# ans = 0
# solve(0, 0)

# print(ans)
