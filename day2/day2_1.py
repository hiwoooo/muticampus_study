#5108 숫자 추가

T=int(input())
arr=[]
for i in range (T):
  N,M,L=map(int,input().split())
  arr=list(map(int, input().split()))
  #print(arr)
  for _ in range(M):
    pos,data=map(int,input().split())
    arr.insert(pos,data)

  print(f'#{i+1} {arr[L]}')

