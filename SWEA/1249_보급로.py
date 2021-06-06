# bfs를 통해 복구 시간이 가장 최소화 되는 경로를 찾아 이동한다.

def check(r, c):
    return 0 <= r < N and 0 <= c < N


def bfs(r, c):
    visited[r][c] = 1
    q = []
    q.append((r, c))
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        qr, qc = q.pop(0)
        for dir in range(4):
            nr = qr + dr[dir]
            nc = qc + dc[dir]
            if check(nr, nc) and visited[nr][nc] == 0:
                visited[nr][nc] = visited[qr][qc] + 1
                # 도착점에 도착했을 시
                if nr == N - 1 and nc == N - 1:
                    return
                q.append((nr, nc))
    
T = int(input())

for tc in range(T):
    N = int(input())
    grid = [list(map(int, list(input()))) for _ in range(N)]
    
    ans = 0
    visited = [[0] * N for _ in range(N)]
    #print(visited)
    visited[0][0] = 1
    minsum = 9999999
    bfs(0, 0)
    
    print(minsum - 1)
    #print(grid[3][3])
    
    





    

    


