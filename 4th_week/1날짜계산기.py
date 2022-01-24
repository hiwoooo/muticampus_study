# 1948. 날짜 계산기

t=int(input())
for i in range(1,t+1):
  M1,D1,M2,D2=map(int,input().split())
  calendar=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  d_day=0
  if M1==M2:
    d_day=D2-D1+1
  elif M1<M2:
    for j in range(M1,M2-1):
      d_day+=calendar[j]
    d_day=d_day+calendar[M1-1]-D1+D2+1

  print(f'#{i} {d_day}')