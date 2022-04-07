# 4047. 영준이의 카드 카운팅

T=int(input())
for t in range(T):
    Test_Case=input()
    card={'S':13, 'D':13, 'H':13, 'C':13}
    card_check=[]

    # S01 D02 H03 H04 
    for i in range(0,len(Test_Case),3): #(카드+번호)마다 슬라이싱
        card_check.append(Test_Case[i:i+3])

    if len(set(card_check))!=len(card_check): #같은문자열이 존재하면 ERROR출력
        print(f'#{t+1} ERROR')
    else:
        for i in range(len(card_check)): #카드무늬갯수만큼 val에서 차감
            card[card_check[i][:1]]=card[card_check[i][:1]]-1 
        print('#{}'.format(t+1), *card.values())


