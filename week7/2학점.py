#1983. 조교의 성적 매기기

def score_sort(score):
    K_score=score[K-1]
    score.sort(reverse=True)
    for i in range(N):
        if score[i]==K_score:
            return grade[int(i/(N/10))]


T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    score=[]
    for n in range(N):
        mid,fin,hw=map(int, input().split())
        score.append(0.35*mid+0.45*fin+0.2*hw)

    print(f'#{t} {score_sort(score)}')
