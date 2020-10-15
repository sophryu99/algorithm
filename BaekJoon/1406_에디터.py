# 문제
# 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

""" ---------- 내 풀이 () ---------- """

from collections import deque

a = list(input())
d = deque()
for i in range(len(a)):
    d.append(a[i])

T = int(input())
idx = -1
params = []
for t in range(T):
    N, M = map(str, input().split())
    params.append(N)
    params.append(M)
    if params[0] == 'L':
        # 커서가 맨 앞이면
        # 왼쪽으로 인덱스 하나 이동
        idx -= 1
        print(d[idx])

    params.clear()

    


