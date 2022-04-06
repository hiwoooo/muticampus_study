#5215. 햄버거 다이어트

T=int(input())
for t in range(T):
    N,L=map(int,input().split())
    taste_cal=[list(map(int, input().split())) for _ in range(N)]

    