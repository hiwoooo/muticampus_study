#10912. 외로운 문자

T=int(input())

for t in range(1,T+1):
    str_case=list(input())

    str_print=sorted(set([s for s in str_case if (str_case.count(s)%2)!=0]))
    if len(str_print)==0 : 
        print(f'#{t} Good')
    else :
        print('#{}'.format(t),''.join(str_print))