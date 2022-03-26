#2007 마디의 길이
T=int(input())
for t in range(1,T+1):
  str=list(input())
  for i in range(1,len(str)+1):
    if str[:i]==str[i:2*i]:
      length=i
      break

  print(f'#{t} {length}')

