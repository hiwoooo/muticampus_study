#3456. 직사각형 길이 찾기

T=int(input())

for t in range(1,T+1):
    a,b,c=map(int, input().split())
    if a==b or a==c:
        d=a+b+c-2*a
    else : d=a+b+c-2*b

    print(f'#{t} {d}')