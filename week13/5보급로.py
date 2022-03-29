#1249. [S/W 문제해결 응용] 4일차 - 보급로

T=int(input())
for t in range(T):
    N=int(input())
    supplyMap=[list(map(int, input().split()))for _ in range(N)]
    S=supplyMap[0][0]
    G=supplyMap[N-1][N-1]

    for i in range(N):
        for j in range(N):
            