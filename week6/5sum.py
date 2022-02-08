#1209. [S/W 문제해결 기본] 2일차 - Sum

def row_max(arr,sum_list):
  for a in arr:
    sum_list.append(sum(a))
  return max(sum_list)

def col_max(arr,sum_list):
  arr=list(map(list,zip(*arr)))
  for a in arr:
    sum_list.append(sum(a))
  return max(sum_list)

def dia_max(arr,sum_list):
  dia_sum=0
  for i in range(100):
    dia_sum+=arr[i][i]
  sum_list.append(dia_sum)
  dia_sum=0
  for i in range(100-1,-1,-1):
    dia_sum+=arr[i][99-i]
  sum_list.append(dia_sum)
  return max(sum_list)

for t in range(1,11):
  T=int(input())
  arr=[list(map(int, input().split()))for _ in range(100)]
  sum_list=[]

  val=[row_max(arr,sum_list), col_max(arr,sum_list), dia_max(arr,sum_list)]

  print(f'#{t} {max(val)}')