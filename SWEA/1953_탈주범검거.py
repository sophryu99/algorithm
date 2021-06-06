
# 갈 수 있는 곳인지 확인
def check(r, c):
    return 0 <= r < N and 0 <= c < M and grid[r][c] != 0

# 파이프 탐색 가능한 방향 확인
def checkPipe(pipeNum):
    # 상하좌우
    if pipeNum == 1:
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 상하
    if pipeNum == 2:
        dx, dy = [0, 0], [-1, 1]
    # 좌우
    if pipeNum == 3:
        dx, dy = [-1, 1], [0, 0]
    # 상우
    if pipeNum == 4:
        dx, dy = [1, 0], [0, -1]
    # 하우
    if pipeNum == 5:
        dx, dy = [1, 0], [0, 1]
    # 하좌
    if pipeNum == 6:
        dx, dy = [-1, 0], [0, 1]
    # 상좌
    if pipeNum == 7:
        dx, dy = [-1, 0], [0, -1]
    
    return dx, dy

def bfs(r, c, L):
    global result
    q = []
    q.append((r,c))
    cnt = 0
    visited[r][c] = 1 
    # 서로 이어지는 파이프들
    pipe = [[1, 1], [1, 2], [1,3], [1,4], [1,5], [1,6], [1,7], [2, 2], [2,4], [2,5], [2, 6], [2, 7], [3, 3], [3, 5], [3, 6], [3,7], [4, 6], [4, 7], [5,7], [6, 7]]

    while q:
        # if hours == (L - 1):
        #     break
        qr, qc = q.pop(0)
        cnt = visited[qr][qc]
        # 방향 어디만 가능한지 정해줘야함
        if cnt < L:
            dx, dy = checkPipe(grid[qr][qc])
            for dir in range(len(dy)):
                nr = qr + dy[dir]
                nc = qc + dx[dir]
                # 조건 통과 시
                if check(nr, nc) and not visited[nr][nc]:
                    # 원래의 파이프와 이동한 파이프의 종류
                    pipe_origin = grid[qr][qc]
                    pipe_new = grid[nr][nc]
                    # 원래의 파이프에서 이동 가능한지 (이어져 있는지) 확인
                    for i in range(len(pipe)):
                        # 이어져 있는 파이프라면
                        if pipe[i][0] == pipe_new and pipe[i][1] == pipe_origin or (pipe[i][1] == pipe_new and pipe[i][0] == pipe_origin):
                            # 이동하기
                            visited[nr][nc] = cnt + 1
                            result +=1
                            q.append((nr, nc))
        
        # hours +=1
        print(cnt)
        print(visited)


T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    result = 1
    visited = [[0] * M for _ in range(N)]
    bfs(R, C, L)
    print("result", result)
    