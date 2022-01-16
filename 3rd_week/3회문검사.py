#1989. 초심자의 회문 검사

T=int(input())
for i in range(1,T+1):
  s=list(input())
  for j in range(len(s)//2):
    if s[j]==s[len(s)-1-j]:
      a=1      
    else : a=0

  print(f'#{i} {a}')