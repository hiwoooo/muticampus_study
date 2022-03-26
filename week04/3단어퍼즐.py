#1979 어디에 단어가 들어갈수 있을까

t=int(input())
for i in range(1,t+1):
  N,K=map(int,(input().split()))
  puzzle=[list(map(int,input().split())) for _ in range(N)]
  cnt=0

 
  for j in range(N):
    a=0
    for k in range(N):
      if puzzle[j][k]==1:
        a+=1
      if puzzle[j][k]==0 or j==N-1:
        if a==K: 
          cnt+=1
        
  for j in range(N):      
    b=0
    for k in range(N):
      if puzzle[k][j]==1:
        b+=1
      if puzzle[k][j]==0 or k==N-1:
        if b==K: 
            cnt+=1
    
  print(f'#{i} {cnt}')      