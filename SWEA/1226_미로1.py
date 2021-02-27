# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(10):
    answer = 0
    n = int(input())
    maps = [list(input()) for _ in range(16)]

    
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if maps[i][j] == '2':                   # 출발점 찾은 후 인덱스 저장
                x, y = i, j

                                                    # DFS 탐색 시작
    stack = [(x, y)]                                
    while stack:                                    # 스택이 존재 할 때
        cx, cy = stack.pop()                        # 스택에 있는 첫 번째 인덱스를 가져온다            
        
        for k in range(4):                          # 상하좌우 탐색 시작
            nx = cx + dx[k]                         # 탐색 후 재 설정된 row index
            ny = cy + dy[k]                         # 탐색 후 재 설정된 col index
            if 0 <= nx < 16 and 0 <= ny < 16:       # 전체 미로의 크기 안에서 탐색
                if maps[nx][ny] == '0':             # 재설정된 인덱스의 미로 값이 0, 즉 길이면
                    stack.append((nx, ny))          # 탐색을 위해 stack에 append
                    maps[nx][ny] = '4'              # 이미 탐색한 길이니 0이 아닌 다른 숫자로 재설정해준다
                elif maps[nx][ny] == '3':           # 재설정된 인덱스의 미로 값이 3, 즉 도착점이면ㄴ
                    answer = 1                      # answer = 1
                    stack.clear()               
                    break                           # 탐색 종료

    print('#{} {}'.format(n, answer))   
