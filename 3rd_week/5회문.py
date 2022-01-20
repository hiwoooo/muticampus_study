# 1215. [S/W 문제해결 기본] 3일차 - 회문1 

L=int(input())
t_case= [list(input()) for _ in range(8)]
cnt=0
for i in range(1):
  for j in range(8-L+1): 
    for k in range(L//2):
      if t_case[i][j+k]==t_case[i][L+j-k-1]:
        cnt+=1
        print(t_case[i][j:j+L])

for i in range(8-L+1):
  for j in range(8):
    for k in range(L//2):
      if t_case[i+k][j]==t_case[i+L-k-1][j]:
        cnt+=1


print(cnt)

##테스트로 첫번째행만 회문 문자만 출력하도록 해봄
#입력
#4
#CBBCBAAB
#CCCBABCB
#CAAAACAB
#BACCCCAC
#AABCBBAC
#ACAACABC
#BCCBAABC
#ABBBCCAA

#출력
#['C', 'B', 'B', 'C']
#['C', 'B', 'B', 'C']
#['B', 'B', 'C', 'B']
#['B', 'A', 'A', 'B']
#['B', 'A', 'A', 'B']
#32
#왜이러는거죠..