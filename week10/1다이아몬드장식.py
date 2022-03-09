#4751. 다솔이의 다이아몬드 장식

T=int(input())
for t in range(1,T+1):
    deco='.#.'
    deco=deco.join(input())
    deco=deco.join(('#.','.#'))

    print('..#.'*(len(deco)//4), end='.\n')
    print('.#'*(len(deco)//2), end='.\n')    
    print(deco)
    print('.#'*(len(deco)//2), end='.\n')
    print('..#.'*(len(deco)//4), end='.\n')

