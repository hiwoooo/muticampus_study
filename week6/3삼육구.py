#1926 369게임


N=int(input())
check=['3','6','9']

for i in range(1,N+1):
  cnt=0
  for j in str(i):
    if j in check:
      cnt+=1
    
  if cnt!=0:
    i='-'*cnt

  print(i, end=' ')
    
    
         