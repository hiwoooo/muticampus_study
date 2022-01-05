# 2.연월일달력

n=int(input())
D= [str(input()) for _ in range(n)]

for i in range(n):
  y=D[i][:4]
  m=D[i][4:6]
  d=D[i][6:]
  if m in {'01','03','05','07','08','10','12'}:
    if int(d)<=31 and int(d)>0:
      print(f'#{i+1} {y}/{m}/{d}')
    else : print(f'#{i+1} -1')
  elif m in {'04','06','09','11'}:
    if int(d)<=30 and int(d)>0:
      print(f'#{i+1} {y}/{m}/{d}')
    else : print(f'#{i+1} -1')
  elif m in {'02'}:
    if int(d)<=28 and int(d)>0:
      print(f'#{i+1} {y}/{m}/{d}')
    else : print(f'#{i+1} -1')
  else : print(f'#{i+1} -1')

#너무 지저분.. 더 간결하게 표현할수 없나....