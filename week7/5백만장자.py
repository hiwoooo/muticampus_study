# 1859. 백만 장자 프로젝트
                

T=int(input())
for t in range(1,T+1):
    N=int(input())
    trade=list(map(int, input().split()))
    prof=0

    while len(trade)>1:
        for i in range(len(trade)):
            if i ==trade.index(max(trade)):
                prof+=max(trade)*i-sum(trade[:i])
                trade=trade[i+1:]
                break

    
    print(f'#{t} {prof}')

#런타임초과..