#2001 파리퇴치

T=int(input())
for t in range(1,T+1):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split()))for _ in range(N)]
    sum_list=[]
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            swat=list(row [j:j+M] for row in arr[i:i+M])
            swat=sum(swat,[])
            sum_swat=0
            for k in range(len(swat)):
                sum_swat += swat[k]
            sum_list.append(sum_swat)
    print(f'#{t} {max(sum_list)}')


    
