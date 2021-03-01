import time
start_time = time.time()
T = int(input())

for tc in range(T):
    N = int(input())
    grid = [list(input().split()) for _ in range(N)]
    diction = dict()

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    maxsum = 0

    # dfs on every point on grid
    for row in range(N):
        for col in range(N):
            cnt = 1
            if int(grid[row][col]) > 0:
                stack = [(row, col)]
                while stack:
                    cx, cy = stack.pop()
                    for k in range(4):
                        # new index
                        nx = cx + dx[k]       
                        ny = cy + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            # if diff is 1
                            if int(grid[cx][cy]) + 1 == int(grid[nx][ny]):
                                cnt += 1
                                stack.append((nx, ny))
                                grid[cx][cy] = "-1"
                                break
            
            diction[grid[row][col]] = cnt
    
            if cnt >= maxsum:
                maxsum = cnt

    minval = 0
    for w in sorted(diction, key=diction.get, reverse=True):
        minval = w
        break
    
    print("#{} {} {}".format(tc+1, minval, maxsum))

print("--- %s seconds ---" % (time.time() - start_time))



    
