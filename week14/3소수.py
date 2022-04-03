#3131. 100만 이하의 모든 소수

N=10**6

a=[1]*(N+1)
a[0], a[1]=0,0
primes=[]
for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j]=False
print(*primes)