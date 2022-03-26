# 1946. 간단한 압축 풀기

T=int(input())
for t in range(1,T+1):
    N=int(input())
    docu=''
    
    for n in range(N):
        c,k= input().split()
        docu+=c*int(k)
    
    print(f'#{t}')
    for i in range(len(docu)//10+1):
        print(docu[10*i:10*i+10])
    