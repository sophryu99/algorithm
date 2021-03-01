
def check(y, x):
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)

def bfs(y, x):
    global result
    q = []
    q.append((y, x))
    visited.append((y, x))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        # 가장 첫 번째 좌표 뽑기
        vy, vx = q.pop(0)
        for dir in range(4):
            # 새로 움직인 좌표
            nx = vx + dx[dir]
            ny = vy + dy[dir]
            # 조건을 통과하면
            if check(ny, nx) and (ny, nx) not in visited:
                q.append((ny, nx))
                visited.append((ny, nx))
                if maze[ny][nx] == 3:
                    result = 1


for tc in range(10):
    T = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    start_y = 0
    start_x = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_y = i
                start_x = j
                break
    result = 0
    visited = []
    bfs(start_y, start_x)
    print("#{} {}".format(tc + 1, result))



