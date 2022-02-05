#1974 스도쿠 검증

def row_search(arr):
    cnt=0
    for i in range(9):
        if len(set(arr[i]))==9:
            cnt+=1
    if cnt==9: return 1
    else : return 0

def col_search(arr):
    cnt=0
    arr=list(map(list,zip(*arr)))
    for i in range(9):
        if len(set(arr[i]))==9:
            cnt+=1
    if cnt==9 : return 1
    else : return 0

def slicing(arr):
    cnt=0
    for i in range(0,9-3+1,3):
        for j in range(0,9-3+1,3):
            arr=list(row [j:j+3] for row in sdk[i:i+3])
            if len(set(sum(arr, [])))==9:
                cnt+=1
    if cnt==9: return 1
    else : return 0


T=int(input())
for t in range (1,T+1):
    sdk=[list(map(int, input().split())) for _ in range(9)]

    if row_search(sdk)+col_search(sdk)+slicing(sdk)==3:
        print(f'#{t} 1')
    else : print(f'#{t} 0')
