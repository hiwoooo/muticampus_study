# 5. 지그재그 숫자
n=int(input())
N=[int(input())for _ in range(n)]

for i in range(n):
  t=0
  while N[i]>0:
    if N[i]%2==1:
      t+=N[i]
    else : t-=N[i]
    N[i]-=1
  print(f'#{i+1} {t}')
