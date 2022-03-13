#10200 구독자 전쟁

def sub_min(N,A,B):
    if (A+B)-N<0:
        return 0
    else : return (A+B)-N

def sub_max(N,A,B):
    if A>B:
        return B
    else : return A

T=int(input())
for t in range(1,T+1):
    N,A,B=map(int, input().split())

    print(f'#{t} {sub_max(N,A,B)} {sub_min(N,A,B)}')
        