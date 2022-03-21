#5789. 현주의 상자 바꾸기

T=int(input())

for t in range(1,T+1):
    N,Q=map(int,input().split())
    box=[0]*N
    for i in range(1,Q+1):
        L,R=map(int,input().split())
        #i는 1부터, 리스트는 0부터 시작
        box[L-1:R]=[i]*(R-L+1)
        
    print('#{}'. format(t),*box)