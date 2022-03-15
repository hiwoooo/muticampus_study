#1221. [S/W 문제해결 기본] 5일차 - GNS

T=int(input())

for t in range(1,T+1):
    N,len=input().split()
    num_series=list(map(str,input().split()))
    str_num={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    num_str={v:k for k,v in str_num.items()}
    change=[]

    for n in num_series:
        change.append(str_num[n])

    change.sort()
    change=list(num_str.get(x) for x in change)

    print(f'#{t}')
    print(*change)