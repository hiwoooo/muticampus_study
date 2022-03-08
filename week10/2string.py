#1213 [S/W 문제해결 기본] 3일차 - String

for t in range(1,3):
    n=int(input())
    search_str=input()
    statement=input()
    cnt=statement.count(search_str)


    print(f'#{t} {cnt}')