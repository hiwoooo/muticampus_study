#5215. 햄버거 다이어트

T=int(input())
for t in range(T):
    N,L=map(int,input().split())
    taste_cal=[list(map(int, input().split())) for _ in range(N)]


    for i in range(N):
        taste_cal[i].append(taste_cal[i][0]/taste_cal[i][1])
    
    taste_cal.sort(key=lambda x: x[2], reverse=True)

    cal_sum=0
    taste_score=0
    for i in range(N):
        cal_sum+=taste_cal[i][1]
        if cal_sum<=L:           
            taste_score+=taste_cal[i][0]
        else : 
            cal_sum-=taste_cal[i][1]
            continue

    print(f'#{t+1} {taste_score}')


    


def hamburger(i, j, )