#10726. 이진수 표현

T=int(input())
for t in range(T):
    N,M=map(int,input().split())

    #bin(30)='0b11110'
    change_binary=list(bin(M)[2:])
    if change_binary[-N:]==(['1']*N):
        print(f'#{t+1} ON')
    else : print(f'#{t+1} OFF')