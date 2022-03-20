for t in range(10):
    N=int(input())
    buildings=list(map(int,input().split()))
    view_sum=0

    #양옆 두칸씩 비교해서 조망권 확보되는지 확인
    #조망권은 i번째가 가장 높을 때 다음 높은 빌딩높이 뺀 값
    for i in range(2,N-2):
        heighst_building=max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
        if max(buildings[i-2:i+3])==buildings[i]:
            view_sum=view_sum+(buildings[i]-heighst_building)
        else : view_sum=view_sum
    
    print(f'#{t+1} {view_sum}')