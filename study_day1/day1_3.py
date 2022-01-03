# 3. 평균값구하기

n= int(input())
a=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  sum=0
  for j in range(10):
    sum+=a[i][j]
    ave=round(sum/10)
  print(f'#{i+1} {ave}')