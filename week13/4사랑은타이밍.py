#4299. 태혁이의 사랑은 타이밍

T=int(input())
for t in range(T):
    D,H,M=map(int,input().split())

    if D==11 and H==11 and M==11:
        wait_min=0
    elif D==11 and H*60+M<11*60+11 :
        wait_min=-1
    else :
        wait_min=H*60+M-(11*60+11)+(D-11)*24*60

    print(f'#{t+1} {wait_min}')
