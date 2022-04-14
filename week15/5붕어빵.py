#1860. 진기의 최고급 붕어빵

def sale_bread(M,K,customer): 
    cnt=0
    while customer:
        bread=(customer[0]//M)*K-cnt #손님수만큼 빼고 난 후의 붕어빵
        if bread<1:
            return "Impossible"
        else: 
            cnt+=1
            customer.pop(0)
    return "Possible"


T=int(input())
for t in range(T):
    N,M,K=map(int, input().split())
    customer=sorted(list(map(int,input().split())))
    
    result=sale_bread(M,K,customer)

    print(f'#{t+1} {result}')


        