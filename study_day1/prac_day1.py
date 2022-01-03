# SW Academy
#2072. 홀수만 구하기

t=int(input())

a=[list(map(int, input().split())) for _ in range(t) ]

for i in range(t):
  sum=0
  for j in range(10):
    if a[i][j]%2==1: 
      sum+=a[i][j]
  
  print(f'#{i+1} {sum}')