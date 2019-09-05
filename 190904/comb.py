N,M  = 5, 3
v = [0 for _ in range(N)]
case = []
cases = []

def comb(d,s): # depth, startindex
    if d == M:
        if len(case) == 3:
            cases.append([*case])
        return
    for i in range(s,N):
        case.append(i)
        comb(d+1,s+1)
        case.pop()
        comb(d+1,s+1)

comb(0,0)
print(cases)

def comb2(d,s): # depth, startindex, yield
    if d == M:
        if len(case) == 3:
            yield [*case]
    else:    
        for i in range(s,N):
            case.append(i)
            yield from comb2(d+1,s+1)
            case.pop()
            yield from comb2(d+1,s+1)

comb2(0,0)

for c in comb2(0,0):
    print(c)