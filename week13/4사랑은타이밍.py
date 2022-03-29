#4299. 태혁이의 사랑은 타이밍

T=int(input())
for t in range(T):
    D,H,M=map(int,input().split())

    wait_min=H*60+M-(11*60+11)+(D-11)*24*60
    if wait_min>=0:
        print(f'#{t+1} {wait_min}')
    else :
        print(f'#{t+1} -1')