# 5948. 새샘이의 7-3-5 게임

T=int(input())
for t in range(T):
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)

    max_5th=arr[0]+arr[1]+arr[-1]

    print(f'#{t+1} {max_5th}')