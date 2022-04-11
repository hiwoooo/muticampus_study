#1860. 진기의 최고급 붕어빵

def sale_bread(M,K):
    global N_list,m
    bread=(N_list[0]//m)*K
    if M>N_list[0]:
        return 0
    elif len(N_list)<=bread :
        return 1 
    else :
        while bread:
            N_list.pop(0)
            bread-=1
        return sale_bread(M+M,K)

T=int(input())
for t in range(T):
    N,M,K=map(int, input().split())
    N_list=sorted(list(map(int,input().split())))
    m=M
    
    if sale_bread(M,K)==1:
        print(f'#{t+1} Possible')
    else : print(f'#{t+1} Impossible')

# 999/1000 ....

        