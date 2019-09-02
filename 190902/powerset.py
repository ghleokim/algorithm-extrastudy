# powerset with binary numbers

a = [1,2,3]

N = 3
for i in range(2**N):
    for j in range(N):
        print(bin(i), bin(1 << j))

        if i & (1 << j):
            print(a[j], end='')
        
    print()
