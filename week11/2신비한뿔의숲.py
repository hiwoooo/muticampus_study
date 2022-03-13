#3142. 영준이와 신비한 뿔의 숲

T=int(input())
for t in range(1,T+1):
    n,m=map(int,input().split())

    uni=m*2-n
    twin=m-uni

    print(f'#{t} {uni} {twin}')