# https://www.acmicpc.net/problem/1890

def check(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs():
    global count
    q = []
    q.append((0, 0, mapp[0][0]))
    visited.append((0, 0))

    while q:
        qr, qc, move = q.pop()
        dx, dy = [move, 0], [0, move]
        for dir in range(2):
            nr = qr + dx[dir]
            nc = qc + dy[dir]
            if check(nr, nc) and (nr, nc) not in visited:
                if mapp[nr][nc] == 0:
                    count += 1
                    #print("done")
                    break
                #print(nr, nc, mapp[nr][nc])
                q.append((nr, nc, mapp[nr][nc]))
                visited.append((nr, nc))
                    

N = int(input())

mapp = [list(map(int, input().split())) for _ in range(N)]

visited = []
count = 0
bfs()
print(count)

