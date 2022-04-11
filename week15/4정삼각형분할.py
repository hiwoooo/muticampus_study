#3233. 정삼각형 분할 놀이

T=int(input())
for t in range(T):
    A,B=map(int, input().split())
    n=int(A/B)

    #2n-1
    ans=0
    for i in range(1,n+1):
        ans+=(2*i-1)

    print(f'#{t+1} {ans}')