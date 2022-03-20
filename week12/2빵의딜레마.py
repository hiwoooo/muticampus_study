#5162. 두가지 빵의 딜레마

T=int(input())

for t in range(1,T+1):
    A,B,C=map(int,input().split())

    #갯수만 많으면 된다=가장 저렴한 빵 여러개 구입
    print(f'{t} {C//min(A,B)}')