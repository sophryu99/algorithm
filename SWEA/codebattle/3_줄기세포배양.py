dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


T = int(input())
for test_case in range(1, 1 + T):
    N, M, K = map(int, input().split())
    my_map = [list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (M + K) for _ in range(K)]
    active = ['dummy'] + [[] for _ in range(10)]  # 생명력 1 ~ 10
    result = 0
    # active 채워 넣기
    for i in range(N):
        for j in range(M):
            if my_map[i][j]:
                active[my_map[i][j]].append([i, j, my_map[i][j]])
    # K만큼 시간 지남
    for _ in range(K):
        for power in range(10, 0, -1):  # 생명력이 높은 순으로 번식
            cells = active[power]
            new = []
            old = []
            for i in range(len(cells)-1, -1, -1):
                cells[i][2] -= 1  # HP 감소
                y, x, HP = cells[i]
                if HP == -1:  # 활성 시작, 번식
                    for d in range(4):
                        ny, nx = (y + dy[d]) % (N + K), (x + dx[d]) % (M + K)
                        if not my_map[ny][nx]:
                            my_map[ny][nx] = power
                            new.append([ny, nx, power])
                if HP == - power:  # 비활성
                    old.append(i)

            for idx in old:  # 비활성 셀 삭제
                cells.pop(idx)
            cells += new  # 번식 셀 추가
    
    # 활성 셀 개수 세기
    result = 0
    for i in range(1, 11):
        result += len(active[i])
        
    print('#{} {}'.format(test_case,result))