T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    s=arr[M%N]

    print(f'#{i+1} {s}')