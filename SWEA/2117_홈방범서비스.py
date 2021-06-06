
def bfs(y, x):
    print(y, x)
    # 전체 맵을 커버하는 다이아몬드 만들기
    radius = N // 2
    




T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    # 집이 있는 곳을 기준으로 탐색 시작

    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 1:
                bfs(i, j)


