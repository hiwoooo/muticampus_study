#3499 퍼펙트 셔플

T=int(input())
for t in range(1,T+1):
    N=int(input())
    card=list(map(str, input().split()))

    card_shuffle=[]
    card1=card[:N//2]
    card2=card[N//2:]
    for i in range(N//2):
        card_shuffle.append(card1[i])
        card_shuffle.append(card2[i])
    
    print('#{}'.format(t), *card_shuffle)

