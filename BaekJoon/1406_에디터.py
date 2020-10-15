# 문제
# 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

""" ---------- 내 풀이 (pass) ---------- """

# 접근: 두개의 stack을 슬라이싱 해서 운영하는 느낌이다. 커서가 움직일 때마다 왼쪽에 있는 스택에서 오른쪽에 있는 스택으로 알파벳들이 왔다갔다 한다고 보면 된다.
# 자세한 설명: 블로그 참조

import sys

lst = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())

left = []
right = []

for i in range(len(lst)):                               # 초기 뎈 생성
    left.append(lst[i])

for i in range(N):
    command = sys.stdin.readline().rstrip().split()    # 입력 값 파싱해서 받기
    if command[0] == "P":                              # P를 받았을 때 그 다음 문자를 왼쪽에 추가
        left.append(command[1])
    elif command[0] == "L":                             # L을 받았을 때
        if len(left):
            move = left.pop()                           # left의 마지막 element를 팝하고
            right.append(move)                          # right에 추가해준다
    elif command[0] == "D":                             # D를 받았을 때 
        if len(right):
            move = right.pop()                          # right의 element를 팝하고
            left.append(move)                           # left에 추가해준다
    else:
        if len(left):
            left.pop()                                  # B를 받았을 때 왼쪽 원소 pop
    
print(''.join(left+right[::-1]))

