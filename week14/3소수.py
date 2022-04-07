#3131. 100만 이하의 모든 소수

#에라토스테네스의 체
N=10**6

a=[1]*(N+1) #0~N까지 1로
a[0], a[1]=0,0  
primes=[]
for i in range(2,N+1):
    if a[i]:
        primes.append(i) #값이 1인 위치값만 추가
        for j in range(2*i, N+1, i): #2*i부터 i배수인 자리 모두 0으로 치환
            a[j]=0
print(*primes)