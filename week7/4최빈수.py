#1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T=int(input())
for t in range(1,T+1):
    a=int(input())
    score_list=list(map(int,input().split()))
    cnt=[0]*101

    for s in score_list:
        cnt[s]+=1
    
    val=max(cnt)

    for i in range(101):
        if cnt[i]==max(cnt):
            val=i

    print(f'#{t} {val}')

