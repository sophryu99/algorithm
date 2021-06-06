# https://www.acmicpc.net/problem/2579

"""
한번에 한 계단 혹은 두 계단 오를 수 있음

"""
T = int(input())

ladder = []
# [10, 20, 15, 25, 10, 20]

# 계단 리스트 생성
for tc in range(T):
    N = int(input())
    ladder.append(N)

# 계단 밟는 리스트 생성
visited = [0] * T
visited[-1] = ladder[-1]

# 1이 연속됐는지 확인하는 리스트
track = 1
i = T - 1
# 도착점에서부터 탐색 시작
while i > 0 and len(ladder) > 1:
    one = 0
    two = 0
    # 한 칸 움직였을 때
    if track < 2:
        one = visited[i] + ladder[i - 1] 
    # 두칸 움직였을 때
    if i != 1:
        two = visited[i] + ladder[i - 2]
    if one >= two:
        # 연속된 1의 개수 더해주기
        track += 1
        visited[i - 1] = one
        i = i - 1
    else:
        track = 1
        visited[i - 2] = two
        # 한칸 더 옮겨주기
        i = i - 2

if len(ladder) == 1:
    print(ladder[0])
elif visited[0] == 0 and len(ladder) > 1:
    print(visited[1])   
else:
    print(visited[0])





        



