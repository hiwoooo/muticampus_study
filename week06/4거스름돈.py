#1970. 쉬운 거스름돈

T=int(input())
for t in range(1,T+1):
  N=int(input())
  money=[50000,10000,5000,1000,500,100,50,10]
  cnt=[0]*8
  for i in range(8):
    if N>=10:
      cnt[i]=N//money[i]
      N=N-money[i]*cnt[i]
  
  print(f'#{t}')
  print(*cnt)