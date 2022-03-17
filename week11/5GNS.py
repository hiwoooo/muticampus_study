#1221. [S/W 문제해결 기본] 5일차 - GNS

T=int(input())

for t in range(1,T+1):
    N,len=input().split()
    num_series=list(map(str,input().split()))
    str_num={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    num_str={v:k for k,v in str_num.items()} #str_num 의 key,value전환
    #num_str={0:"ZRO", 1:"ONE", 2:"TWO", ~ }
    change=[]

    for n in num_series:
        change.append(str_num[n]) #입력받은 문자열을 딕셔너리의 value 리스트 생성

    change.sort() #숫자리스트 정렬
    change=list(num_str[x] for x in change) #숫자를 다시 문자열로
    #num_str[x]==num_str.get(x)

    print(f'#{t}')
    print(*change)