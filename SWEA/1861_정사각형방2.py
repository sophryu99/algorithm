# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# D4

# N의 크기가 엄청 커지면 런타임 에러 뜸

def check(y, x):
    return 0 <= y < N and 0 <= x < N and (y, x) not in visited


def dfs(y, x):
    global maxdist
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if check(ny, nx) and mapp[ny][nx] - mapp[y][x] == 1:
            visited.append((ny, nx))
            #visited[ny][nx] = visited[y][x] + 1
            if visited[ny][nx] > maxdist:
                maxdist = visited[ny][nx]
            #print(visited)
            dfs(ny, nx)
            visited[ny][nx] = 0
            #print('end', visited)
            

T = int(input())

for tc in range(T):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    #visited = [[0] * N for _ in range(N)]
    visited = []
    startpoint = 0
    maxdist = 0
    for i in range(N):
        for j in range(N):
            #visited[i][j] = 1
            dfs(i, j)
            #visited[i][j] = 0
    
    print(maxdist)
