#1959. 두 개의 숫자열

T=int(input())
for i in range(1,T+1):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  if N<M:
   arr=[]
   for k in range(M-N+1):
     m=0
     for j in range(N):
       m+=A[j]*B[k+j]
     arr.append(m)
   arr.sort()
   print(f'#{i} {arr[-1]}')
 
  elif N>M:
    arr=[]
    for k in range(N-M+1):
      m=0
      for j in range(M):
        m+=A[j+k]*B[j]
      arr.append(m)
    arr.sort()
    print(f'#{i} {arr[-1]}')

  else :
    m=0
    for j in range(N):
      m+=A[j]*B[j]
    print(f'#{i} {m}')