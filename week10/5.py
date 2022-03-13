#11688 Calkin-Wilf tree 1

T=int(input())

for t in range(1,T+1):
    TreeNode=input()
    a=1
    b=1

    for i in range(len(TreeNode)+1):
        if TreeNode[i:i+1]=='L':
            a=a
            b=a+b
        elif TreeNode[i:i+1]=='R':
            a=a+b
            b=b

    print(f'#{t} {a} {b}')    