# 5948. 새샘이의 7-3-5 게임

T=int(input())
for t in range(T):
    arr=list(map(int,input().split()))
    arr_sum=[]

    #앞에서부터 3개씩 합(0,1,2),(0,1,3),(0,1,4),...
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                arr_sum.append(arr[i]+arr[j]+arr[k])

    print(f'#{t+1} {sorted(set(arr_sum),reverse=True)[4]}')