# https://www.acmicpc.net/problem/16234

import sys

N, L, R = map(int, sys.stdin.readline().split())
mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


visited = [[0] * N for _ in range(N)]

def check(r, c):
    return 0 <= r < N and 0 <= c < N and not visited[r][c]


def bfs(r, c):
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]
    q = []
    q.append((r, c))

    population = 0
    while q:
        qr, qc = q.pop(0)
        for dir in range(4):
            nr = qr + dr[dir]
            nc = qc + dc[dir]
            if check(nr, nc) and L <= abs(mapp[nr][nc] - mapp[qr][qc]) <= R:
                q.append((nr, nc))
                



