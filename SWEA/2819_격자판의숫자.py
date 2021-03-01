# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

def dfs(idx,row,col,num):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    num += mapp[row][col]
    if idx == 6:                                        # 6번 이동한 결과 값 result 배열에 추가
        result.append(num)
        return
    for i in range(4):
        if 0 <= row+dx[i] < 4 and 0 <= col+dy[i] < 4:   # 벽 체크
            dfs(idx+1,row+dx[i],col+dy[i],num)
 
T = int(input())
for t in range(T):
    mapp = [list(map(str,input().split())) for _ in range(4)]
    result = []                                         # 결과값 저장 될 배열
    for x in range(4):
        for y in range(4):
            dfs(0,x,y,"")
 
    answer = set(result)                                # 중복 제거를 위해 set 사용
    print('#{} {}'.format(t+1,len(answer)))