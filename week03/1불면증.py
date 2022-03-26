#1288. 불면증 치료법

T=int(input())
for i in range(1,T+1):
  N=int(input())
  arr=[]
  cnt=0
  if N>=1 and N<=1000000:
    while 1:
      cnt+=1
      arr+=list(map(int, str(N*cnt)))
      
      if set(arr)=={0,1,2,3,4,5,6,7,8,9}: break

    print(f'#{i} {N*cnt}')