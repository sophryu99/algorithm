# D4, DFS
# 도착점을 출발점으로 생각하면 된다. 도착점에서 DFS 진행하면서 row = 0 이 될때까지 탐색한다.

def check(y, x):
    return 0 <= y < L and 0 <= x < L and mapp[y][x] == 1

def dfs(y, x):
    global y_start, x_start
    # 출발점에 도착했을 경우
    if y == 0:
        y_start = y
        x_start = x
        return
    
    # 왼쪽, 오른쪽, 위쪽만
    dx, dy = [-1, 1, 0], [0, 0, -1]
    
    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]
        #print(ny, nx)
        if check(ny, nx) and (ny, nx) not in visited:
            visited.append((ny, nx))
            print(visited)
            dfs(ny, nx)
            visited.remove((ny, nx))
            

for tc in range(10):
    N = int(input())
    L = 5
    mapp = [list(map(int, input().split())) for _ in range(L)]
    y_end = 0
    x_end = 0
    y_start = 0
    x_start = 0
    visited = []
    for i in range(L):
        for j in range(L):
            if mapp[i][j] == 2:
                y_end = i
                x_end = j
                break
            
    dfs(y_end, x_end)
    print(y_start, x_start)    
