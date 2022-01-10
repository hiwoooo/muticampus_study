#5108 숫자 추가

T=int(input())
arr=[]
for i in range (T):
  N,M,L=map(int,input().split())
  arr=list(map(int, input().split()))
  #print(arr)
  for _ in range(M):
    pos,data=map(int,input().split())
        #insertData(pos,data)
    arr.append(None)
    N+=1
    for j in range(N-1,pos,-1):
      arr[j]=arr[j-1]
      arr[j-1]=None
    arr[pos]=data
    #print(arr)
   

  print(f'#{i+1} {arr[L]}')
