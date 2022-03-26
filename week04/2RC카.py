#1940 RC카

T=int(input())
for t in range(1,T+1):
  N=int(input())
  v=0
  d=0
  for i in range(N):
    command=list(map(int,input().split()))
    if command[0]==0:
      v=v
      d+=v
    elif command[0]==1:
      v+=command[1]
      d+=v
    elif command[0]==2:
      if command[1]>v:
        v=0
        d=d
      else:
        v-=command[1]
        d+=v

  print(f'#{t} {d}')
