#11736. 평범한 숫자

#p1~pn의 순열에서 pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi를 평범한 숫자라고 정의

T=int(input())
for t in range(T):
    N=int(input())
    Permutation=list(map(int,input().split()))
    cnt=0

    for i in range(1,N):
        if Permutation[i]!=min(Permutation[i-1:i+2]) and Permutation[i]!=max(Permutation[i-1:i+2]):
            cnt+=1
    
    print(f'#{t+1} {cnt}')

