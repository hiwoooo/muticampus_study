#10761 신뢰

#B가 누르는동안 O가 미리 이동 가능


T=int(input())
for t in range(T):
    arr=list(map(int,input().split()))
    
    test_time=0
    
    for i in range(1,len(arr)-2):
        if arr[i]=='B':
            test_time+=arr[i+1]
