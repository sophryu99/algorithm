T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))                        # 시험 답안
    student = [list(map(int, input().split())) for _ in range(N)]   # 학생들 답안 이차원 배열로 받기
    studentT = list(map(list, zip(*student)))                       # 한 row가 한 문제에 대한 모든 학생들의 답
    score = [[0] * N for _ in range(M)]                             # 점수기록용 배열
    
    for j in range(M):
        for i in range(N):
            if answer[j] == studentT[j][i]:
                if j == 0:
                    score[j][i] = 1
                score[j][i] = score[j-1][i] + 1
            else:
                score[j][i] = 0

    
    scoreT = list(map(list, zip(*score)))
    finalscore = []
    for k in scoreT:
        finalscore.append(sum(k))
    print("#{} {}".format(tc + 1, max(finalscore)-min(finalscore)))
