#3142. 영준이와 신비한 뿔의 숲

T=int(input())
for t in range(1,T+1):
    n,m=map(int,input().split())
    #n:뿔수 m:마릿수

    #뿔두개짐승이 m마리면 뿔수=2*m, 부족한만큼 뿔하나
    uni=m*2-n
    twin=m-uni

    print(f'#{t} {uni} {twin}')