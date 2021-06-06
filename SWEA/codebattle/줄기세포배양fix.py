
def bfs():
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    time = 0
    while time < K:
        time += 1
        for k in range(10, 0, -1):
            cells = life[k]
            alive, dead = [], []
            for i in range(len(cells)):
                cells[i][2] -= 1
                y, x, e = cells[i]
                # 활성화된 셀
                if e == -1:
                    # 상하좌우 탐색 시작
                    for dir in range(4):
                        ny = y + dy[dir]
                        nx = x + dx[dir]
                        if not visited[ny][nx] and (ny, nx) not in dead:
                            visited[ny][nx] = k
                            alive.append([ny, nx, k])
                    dead.append((y, x))

            cells += alive 
            for _ in dead:
                cells.pop(0)
            
        
T = int(input())
for tc in range(1, 1 + T):
    N, M, K = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    
    # 각 생명력마다 인덱스 저장할 배열 생성
    life = [[] for _ in range(11)]
    # 배양시간을 고려해서 최대 배양 배열 생성
    visited = [[0] * (M + K) for _ in range(N + K)]
    
    result = 0
    for i in range(N):
        for j in range(M):
            life[mapp[i][j]].append([i, j, mapp[i][j]])
            # 가운데로 옮겨주기
            visited[i + K // 2 + 1][j + K // 2 + 1] = mapp[i][j]

    bfs()
    
    for res in range(1, 11):
        result += len(life[res])
        
    print('#{} {}'.format(tc, result))