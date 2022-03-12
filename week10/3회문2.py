#1216. [S/W 문제해결 기본] 3일차 - 회문2

def findmax(puzzle):
    global maxlen
    for i in range(100):
        for j in range(100):
            for k in range(100,1,-1):
                if puzzle[i][j:k]==puzzle[i][k-1:j-1:-1]:
                    if maxlen<k-j:
                        maxlen=k-j

for t in range(1,11):
    puzzle=[list(input())for _ in range(100)]
    maxlen=0
    
    findmax(puzzle)
    zippuzzle=list(map(list, zip(*puzzle)))
    findmax(zippuzzle)

    print(f'#{t} {maxlen}')