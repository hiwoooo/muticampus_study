#10761 신뢰

#B가 누르는동안 O가 미리 이동 가능

def robot(B_loc,O_loc,test_time=0):
    if arr[0]=='B':
        if arr[1]>B_loc:
            B_loc=arr[1]
            test_time=arr[1]-B_loc+1   
        elif arr[1]<B_loc:
            B_loc=arr[1]
            test_time=B_loc-arr[1]+1
        else : 
            arr.pop(0)
            arr.pop(0)
        
        if O_loc!=1:
            if O_loc>1:
                O_loc
        
    if arr[0]=='O':
        if arr[1]>O_loc:
            O_loc=arr[1]
            test_time=arr[1]-O_loc+1   
        elif arr[1]<O_loc:
            O_loc=arr[1]
            test_time=O_loc-arr[1]+1
        else : 
            arr.pop(0)
            arr.pop(0)

T=int(input())
for t in range(T):
    arr=list(map(int,input().split()))
    

