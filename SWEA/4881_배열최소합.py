T = int(input())

def isCondition(y, x):
    return 0 <= y < N and 0 <= x < N and visited[x] != 1

def dfs(y, x):

    global pathsum
    global maxsum

    if y == N - 1:
        return

    visited[x] = 1
    # y index는 +1 으로만 이동
    # x index는 왼, 오른쪽으로 이동 가능
    dx = [-1, 1, 0]
    for dir in range(3):
        nx = x + dx[dir]
        ny = y + 1
        if isCondition(ny, nx):
            pathsum += grid[ny][nx]
            dfs(ny, nx)
            print(grid[ny][nx])


for tc in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 세로로 겹치는 인덱스 카운팅
    visited = [0] * N

    pathsum = 0
    maxsum = 0
    for i in range(N):
        dfs(0, i)

    print(pathsum)
    # print(grid[0][1])