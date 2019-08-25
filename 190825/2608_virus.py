# https://www.acmicpc.net/problem/2606
# DFS

V = int(input())
E = int(input())

adj = [[0 for _ in range(V+1)] for __ in range(V+1)]

for _ in range(E):
    s, g = map(int, input().split())
    adj[s][g] = 1
    adj[g][s] = 1

visited = [0 for _ in range(V+1)]

#DFS
stack = [0 for _ in range(V)]
top = -1

top += 1
stack[top] = 1

res = 0

while top != -1:
    current = stack[top]
    stack[top] = 0
    top -= 1

    for num, ad in enumerate(adj[current]):
        if ad and not visited[num]:
            visited[num] = 1
            top += 1
            stack[top] = num

print(sum(visited)-1)