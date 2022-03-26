#1984. 중간 평균값 구하기

T=int(input())
for t in range(1,T+1):
    arr=list(map(int, input().split()))
    arr.sort()

    arr_mean=round(sum(arr[1:9])/8)

    print(f'#{t} {arr_mean}')
    