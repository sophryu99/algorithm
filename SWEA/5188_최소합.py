"""
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
Approach: 완전탐색 (dfs)
"""
T = int(input())

def isCondition(row, col):
    return 0 <= row < N and 0 <= col < N and [row,col] not in visited

def dfs(row, col):
    global totalsum, pathsum
    
    dx, dy = [1, 0], [0, 1]             # 우측, 밑으로만 이동 가능

    if totalsum < pathsum:
        return

    if row == N -1 and col == N - 1:    # 우측 하단에 도착했을 때
        totalsum = pathsum              # totalsum 값 재설정
        return
    
    for dir in range(2):
        nx = row + dx[dir]              # 재설정된 인덱스
        ny = col + dy[dir]
        if isCondition(nx, ny):         
            visited.append((nx, ny))    # visited에 방문한 노드 표시
            pathsum += grid[nx][ny]     # pathsum에 더해주기
            dfs(nx, ny)                 # 재설정된 인덱스로 재귀적 dfs 수행
            visited.remove((nx, ny))    # visited 방문한 노드 초기화
            pathsum -= grid[nx][ny]     # 가장 최근의 갈림길까지의 sum 빼주기

    
        
for tc in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    totalsum = 9876521                  # 임의의 큰 수 설정
    pathsum = grid[0][0]
    visited = []
    dfs(0, 0)                           # 그리드의 좌측 상단에서 탐색 진행
    print("#{} {}".format(tc+1, totalsum))

