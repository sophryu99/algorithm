
N = 3
A = input()

def check(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c):
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if check(nr, nc) and (r, c) not in visited:
            if A[nr][nc] == 7:
                return
            visited.append((nr, nc))
            print(visited)
            dfs(nr, nc)
            visited.remove((nr, nc))

visited = []
dfs(0, 0)