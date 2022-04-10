# 12004. 구구단 1

T=int(input())
for t in range(T):
    N=int(input())

    ans=0
    for i in range(1, 10):
        for j in range(i,10):
            if N==i*j:
                ans=1
                break   
    
    if ans==1:
        print(f'#{t+1} Yes')
    else : print(f'#{t+1} No')