#1493. 수의 새로운 연산

# (1,1) = 1, (2,1)=3, (2,2) = 5, (4,4) = 25
# &(1)=(1,1), &(3)=(2,1), &(5)=(2,2), &(25)=(4,4)
# p★q는 #(&(p)+&(q))
# ex) &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13



def PstarQ(p,q):
    global arr
    s1=[(x,y) for y in range(q+1) for x in range(p+1) if arr[y][x]==p][0] 
    s2=[(x,y) for y in range(q+1) for x in range(p+1) if arr[y][x]==q][0]
    return arr[s1[1]+s2[1]][s1[0]+s2[0]]

arr=[[0 for col in range(80)]for row in range(80)]
for x in range(1,80):
    for y in range(1,80):
        if x==y:
            arr[y][x]=sum([i**2 for i in range(x-1,x+1)])
        elif x==1:
            arr[y][x]=1+sum([i for i in range(y)])
        else: 
            arr[y][x]=arr[y][x-1]+(x+y-1)

T=int(input())

for t in range(T):
    p,q=map(int, input().split())

    print(f'#{t+1} {PstarQ(p,q)}')

