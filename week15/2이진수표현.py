#10726. 이진수 표현

# 정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별

T=int(input())
for t in range(T):
    N,M=map(int,input().split())

    #bin(30)='0b11110'
    change_binary=list(bin(M)[2:])
    if change_binary[-N:]==(['1']*N):
        print(f'#{t+1} ON')
    else : print(f'#{t+1} OFF')