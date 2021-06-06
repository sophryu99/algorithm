
def bfs():
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    totaltime = 0
    while totaltime < K:
        # 시간 카운트 시작
        totaltime += 1
        # 큰 생명력부터 탐색
        for i in range(len(life) - 1 , -1, -1 ):
            # 2부터
            cell = life[i]
            # print('q', cell)
            dead = []
            # 활성화된 세포일 때
            # if span > 0:
            #     # 상하좌우 탐색
            #     for dir in range(4):
            #         nr = qr + dr[dir]
            #         nc = qc + dc[dir]
            #         # 생명력이 0이거나 움직인 곳의 셀이 현재 생명력보다 작을 때
            #         if visited[nr][nc] == 0 or visited[qr][qc] > visited[nr][nc] and (nr, nc) not in dead:
            #             # 번식
            #             visited[nr][nc] = visited[qr][qc]
            #             # 새로운 번식된 셀 생명 리스트에 추가해주기
            #             life[visited[nr][nc]].append((nr, nc, visited[nr][nc]))
            #             # 수명이 0이 되었다면
            #             if visited[qr][qc] == 0:
            #                 # 죽은 것으로 처리
            #                 dead.append((qr, qc))
            #         # 더 큰 생명력의 셀이 존재한다면
            # # 아직 활성화가 되지 않았다면
            # else:
            #     q.append((qr, qc, life, totaltime + 1))




T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    # 세포 배열
    mapp = [list(map(int, input().split())) + [0] * K for _ in range(N)]
    
    # 배양시간을 고려해서 최대 배양 배열 생성
    visited = [[0] * (M + K + 2) for _ in range(N + K + 2)]

    # 생명력 배열
    life = [[] for _ in range(11)]
    q = []

    # 배양 세포 중간으로 옮겨주기
    for i in range(N):
        for j in range(M):
            q.append([i + (K // 2) + 1, j + ( K // 2) + 1, mapp[i][j], 0])
            visited[i + K // 2 + 1][j + K // 2 + 1] = mapp[i][j]
            # 생명력 배열
            life[mapp[i][j]].append([i, j, mapp[i][j]])

    bfs()
    res = 0
    # for k in visited:
    #     print(k, sep = '\n')
    
    print("#{} {}".format(tc + 1, res))

    


