# 12004. 구구단 1

T=int(input())
for t in range(T):
    N=int(input())

    ans=0
    for i in range(1, 10):
        for j in range(i,10): #(1,1) (1,2) (1,3) ... (5,5) (5,6) (5,7) ... (8,9) (9,9)
            if N==i*j:
                ans=1
                break   
    
    if ans==1:
        print(f'#{t+1} Yes')
    else : print(f'#{t+1} No')