
def check(y, x):
    return 0 <= y < N and 0 <= x < N and mapp[y][x] not in visited_num

def bfs(y, x):
    q = []
    q.append((y, x))
    visited_map[y][x] = 1
    visited_num.append(mapp[y][x])

    # 대각선 방향으로 탐색
    dx, dy = [1, 1, -1, -1], [1, -1, 1, -1]
    while q:
        qy, qx = q.pop(0)
        for dir in range(4):
            ny = qy + dy[dir]
            nx = qx + dx[dir]
            if check(ny, nx) and not visited_map[ny][nx]:
                q.append((ny, nx))
                visited_num.append(mapp[ny][nx])
                visited_map[ny][nx] = visited_map[qy][qx] + 1
                print(ny, nx)
                print(visited_num)


T = int(input())

for tc in range(T):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    visited_map = [[0] * N for _ in range(N)]
    visited_num = []
    
    # for i in range(N):
    #     for j in range(N):
    #         bfs(i, j)
    bfs(0, 2)
    
    