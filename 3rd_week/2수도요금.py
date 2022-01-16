#1284 수도요금경쟁

T=int(input())
for i in range(1,T+1):
  P,Q,R,S,W=map(int,input().split())
 
  cost1=P*W
  if W<=R: cost2=Q
  else : cost2=Q+(W-R)*S

  if cost1>= cost2 :
    print(f'#{i} {cost2}')
  else : print(f'#{i} {cost1}')