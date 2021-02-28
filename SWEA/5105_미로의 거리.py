T = int(input())

# check if the new index is within the grid range, and check if next path is either road or the destination
def isCondition(row, col):
    return 0 <= row < N and 0 <= col < N and (maze[row][col] == 0 or maze[row][col] == 3)

def bfs(row, col):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que.append([row, col])
    visited.append((row, col))
    
    global res
    while que:
        qx, qy = que.pop(0)
        for k in range(4):
            nx = qx + dx[k]
            ny = qy + dy[k]
            if isCondition(nx, ny) and (nx, ny) not in visited:
                que.append((nx, ny))
                visited.append((nx, ny))
                distance[nx][ny] = distance[qx][qy] + 1
                if maze[nx][ny] == 3:
                    res = distance[nx][ny] -1
                    return

for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # find the starting point
            if maze[i][j] == 2:
                start_row, start_col = i, j
                break
   
    que = []
    res = 0
    distance = [[0] * N for _ in range(N)] 
    bfs(start_row, start_col)
    print("#{} {}".format(tc+1, res))

