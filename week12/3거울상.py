#10804 문자열의 거울상

T=int(input())

for t in range(1,T+1):
    arr=list(input())
    mirror={'b':'d', 'd':'b', 'p':'q', 'q':'p'}
    #거꾸로 뒤집기
    arr=arr[::-1]
    #해당하는 value 찾아서 문자열로 변환
    arr_mirror=''.join(list(mirror.get(x) for x in arr))
    
    print('#{}'.format(t),arr_mirror)