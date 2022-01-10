T=int(input())
for i in range(T):
    arr=list(input())
    stack=[]
    for data in arr:
        if stack and data==stack[-1]: #Q
            stack.pop()
        else : 
            stack.append(data)

    print(f'#{i+1} {len(stack)}')
