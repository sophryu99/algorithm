# https://www.acmicpc.net/problem/13460
"""
Approach: bfs
빨간공과 파란공의 bfs를 동시에 진행한다.
한번의 탐색마다 빨간색 공과 파란색 공의 위치가 같아서는 안된다.
빨간공과 파란공의 위치는 서로에게 영향을 받는다. 따라서 공들의 현재 위치에 대한 인덱스 역시 저장해야한다.
빨간공과 파란공이 나란히 있을 시 방향마다 인덱스 설정을 다르게 해줘야함. 

한번 기울일때마다 해당 방향으로 탐색 가능한 마지막 인덱스까지 이동한다.
10번 안에 빨간 공이 0에 도달하지 못하면 -1 리턴
파란 공이 빨간공보다 먼저 0에 도달한다면 -1 리턴
빨간 공이 0에 도달할 수 있는 최소 횟수 리턴
"""

# 이동 가능한 좌표인지 확인
def check(y, x):
    # 상하좌우에 빨간공 혹은 파란 공이 있을 떄도 고려해야함
    return (mapp[y][x] == '.' or mapp[y][x] == 'O') and (0 <= y < N and 0 <= x < M)

# 한번에 이동하기
def move(y, x, dir_y, dir_x):
    global cnt
    # 같은 방향으로 한 번 더 이동한 인덱스 재설정
    my = y + dir_y
    mx = x + dir_x
    # 이동 가능한 곳이라면
    if check(my, mx) and (my, mx) not in visited:
        visited.append((my, mx))
        distance[my][mx] = distance[y][x] + 1
        # 0에 도착 시
        if mapp[my][mx] == 'O':
            return -1, cnt
        return move(my, mx, dir_y, dir_x)
    # 이동 불가능하다면 현재의 y, x 값 리턴
    else:
        return (y, x)
    
def play(y, x):
    global cnt
    q = []
    q.append((y, x))
    visited.append((y, x))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        # 가장 첫번째의 좌표 pop
        qy, qx = q.pop(0)
        cnt += 1
        # 상하좌우 탐색해서 새로운 좌표 설정
        for dir in range(4):
            ny = qy + dy[dir]
            nx = qx + dx[dir]
            # 이동 가능한 좌표인지 확인
            if check(ny, nx) and (ny, nx) not in visited:
                if mapp[ny][nx] == 'O':
                    return cnt
                visited.append((ny, nx))
                distance[ny][nx] = distance[qy][qx] + 1
                # 같은 방향으로 더 이동이 가능한지 확인 후 가장 끝의 인덱스로 이동
                fy, fx = move(ny, nx, dy[dir], dx[dir])
                # 탐색 중 0에 도달했을 시
                if fy == -1:
                    return fx
                q.append((fy, fx))
                print('q', q)
                print('v', visited)
                print(distance)


N, M = map(int, input().split())
mapp = [list(map(str, input())) for _ in range(N)]

red_y, red_x = 0, 0
blue_y, blue_x = 0, 0

for n in range(N):
    for m in range(M):
        if mapp[n][m] == 'R':
            red_y, red_x = n, m
        if mapp[n][m] == 'B':
            blue_y, blue_x = n, m
cnt = 0
visited = []
distance = [[0] * M for _ in range(N)]

print(play(red_y, red_x))
#print('blue', play(blue_y, blue_x))


# 한번씩 기울일 때마다의 빨간공과 파란 공의 위치 표시
moved_red = [0] * 10
moved_blue = [0] * 10
