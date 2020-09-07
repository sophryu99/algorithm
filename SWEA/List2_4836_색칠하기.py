# [입력]
 
# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
# color = 1 (빨강), color = 2 (파랑)

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

T = int(input())
for t in range(T):
    N = int(input())
    red = []
    blue = []
    for i in range(N):
        # 좌표 parsing
        x1, y1, x2, y2, color = map(int,input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:
                    red.append((x,y))
                else:
                    blue.append((x,y))
        # 한 리스트에서 다른 리스트의 엘레멘트와 겹칠때 purple list에 추가하기
        purple = []
        for i in red:
            if i in blue:
                purple.append(i)
    print("#{} {}".format(t+1, len(purple)))


    


            