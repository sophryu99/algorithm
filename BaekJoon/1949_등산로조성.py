# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUqs
# [모의 SW 역량테스트] 등산로 조성

def check(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c):
    global k, maxvisit, cut
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if check(nr, nc):
            # 다음 등산로의 높이가 현재 등산로보다 높이가 낮고 탐색 가능하다면
            if mapp[nr][nc] < mapp[r][c] and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                #print("go", visited)
                dfs(nr, nc)
                if visited[nr][nc] > maxvisit:
                    maxvisit = visited[nr][nc]
                visited[nr][nc] = 0
                #print("back", visited)
           
            # 다음 등산로의 높이가 현재 등산로보다 높이가 같거나 높다면
            if mapp[nr][nc] >= mapp[r][c] and visited[nr][nc] == 0 and not cut:
                # 가능한 k 값 내에서 계속 깎아본다
                for i in range(1, K + 1):
                    height = mapp[nr][nc] - i
                    # 깎은 높이가 현재 위치보다 낮아진다면, 아직 깎은 적이 없다면
                    if height < mapp[r][c]:
                        # 공사하기
                        mapp[nr][nc] = height
                        cut = True
                        visited[nr][nc] = visited[r][c] + 1
                        #print("go_cut", visited)
                        # dfs 다시 진행
                        dfs(nr, nc)
                        # 방문한 거리가 가장 멀다면 maxvisit에 저장
                        if visited[nr][nc] > maxvisit:
                            maxvisit = visited[nr][nc]
                        
                        cut = False
                        # 깎은거 다시 원래대로 되돌려놓기
                        mapp[nr][nc] += i
                        visited[nr][nc] = 0 
                        #print("back_cut", visited)



T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    maxval = 0
    
    # 가장 높은 봉우리 탐색
    for i in range(N):
        for j in range(N):
            if mapp[i][j] > maxval:
                maxval = mapp[i][j]
    
    # 가장 높은 봉우리들 저장
    tallidx = []

    for k in range(N):
        for l in range(N):
            if mapp[k][l] == maxval:
                tallidx.append((k, l))
    
    # 이동한 거리 저장
    visited = [[0] * N for _ in range(N)]

    # 가장 먼 거리 저장
    maxvisit = 0

    # 깎았는지 저장
    cut = False

    # 높은 봉우리들에 대해 dfs 진행
    for d in tallidx:
        r, c = d
        visited[r][c] = 1
        dfs(r, c)
        visited = [[0] * N for _ in range(N)]
    
    print("#{} {}".format(tc+1, maxvisit))
    