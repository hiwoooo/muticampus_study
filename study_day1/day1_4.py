# 4. 간단한 소인수분해

n=int(input())
N=[int(input()) for _ in range(n)]

for i in range(n):
  a=0
  while N[i]%2==0:
    N[i]=N[i]/2
    a+=1
  b=0
  while N[i]%3==0:
    N[i]=N[i]/3
    b+=1
  c=0
  while N[i]%5==0:
    N[i]=N[i]/5
    c+=1
  d=0
  while N[i]%7==0:
    N[i]=N[i]/7
    d+=1
  e=0
  while N[i]%11==0:
    N[i]=N[i]/11
    e+=1

  print(f'#{i+1} {a} {b} {c} {d} {e}')