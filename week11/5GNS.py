#1221. [S/W 문제해결 기본] 5일차 - GNS

T=int(input())

for i in range(1,T+1):
    N=int(input())
    num_series=list(map(str,input().split()))
    num_str={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5 , "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    change=[]

    for n in num_series:
        change.append(num_str[n])

    change.sort()

    for n in change:
        num_str.keys(n)