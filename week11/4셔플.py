#3499 퍼펙트 셔플

T=int(input())

for t in range(1,T+1):
    N=int(input())
    card=list(map(str, input().split()))
    card_shuffle=[]
   
    card1=card[:N//2+(N%2)]
    #card2=card[N//2+(N%2):]
    card2=list(set(card)-set(card1))

    for i in range(len(card2)):
      card_shuffle.append(card1[i])
      card_shuffle.append(card2[i])
    if len(card1)>len(card2):
      card_shuffle.append(card1[-1])

    print('#{}'.format(t), *card_shuffle)

    