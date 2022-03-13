#9700. USB 꽂기의 미스터리

T=int(input())

for t in range(1,T+1):
    p,q=map(float,input().split())

    #반대로 꽂고 뒤집어서 성공
    s1=(1-p)*q
    #올바른면 잘못-반대-제대로
    s2=p*(1-q)*q

    if s1<s2:
        print(f'#{t} YES')
    else : print(f'#{t} NO')