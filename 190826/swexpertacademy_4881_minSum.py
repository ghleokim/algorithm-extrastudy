# LEARN > Course > Programming Intermediate > Stack 2
"""
N * N 배열에서 N개의 숫자를 골라 합이 최소가 되도록.
세로로 같은 줄에서 두 개 이상의 숫자를 고르지 않도록 한다.
가지치기 중요.
"""

def perm(k, s=0):
    global res
    if k == N:
        if s < res:
            res = s
    else:
        if s > res:
            # 탈출조건: 현재까지의 sum > 현재까지의 minimum result
            return 0
        for i in range(N):
            if not visited[i]:
                print(i, end=' ')
                # 다음순열
                visited[i] = 1
                s += board[k][i]
                perm(k+1, s)
                # 순열 빠져나옴
                s -= board[k][i]
                visited[i] = 0

for T in range(int(input())):
    N = int(input())
    board = []
    for _ in range(N):
        board.append([*map(int, input().split())])

    # 길이 N의 visited 리스트 생성
    visited = [0 for _ in range(N)]
    target = [0 for _ in range(N)]

    res = 1000000
    perm(0)

    print('#{0} {1}'.format(T+1, res))



"""
TC
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
"""
