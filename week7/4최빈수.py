#1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T=int(input())
for t in range(1,T+1):
    a=int(input())
    score_list=list(map(int,input().split()))
    cnt=[0]*101

    #cnt리스트에 점수별 카운트
    for s in score_list:
        cnt[s]+=1
    
    val=max(cnt)

    #최빈수 여러개면 큰 점수 출력
    for i in range(101):
        if cnt[i]==max(cnt):
            val=i

    print(f'#{t} {val}')

