"""
Approach: DFS
"""
T = int(input())

def isCondition(row, col):
    return 0 <= row < N and 0 <= col < N and (row,col) not in visited and (grid[row][col] == 0 or grid[row][col] == 3)

def dfs(row, col):
    global res

    if grid[row][col] == 3:
        res = 1
        return

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dir in range(4):
        nx = row + dx[dir]
        ny = col + dy[dir]
        if isCondition(nx, ny):
            visited.append((nx, ny))
            dfs(nx, ny)
            visited.remove((nx, ny))

for tc in range(T):

    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    start_x = 0
    start_y = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                start_x, start_y = i, j
                break
    res = 0
    visited = []
    dfs(start_x, start_y)
    print("#{} {}".format(tc+1, res))


