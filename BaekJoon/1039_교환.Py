# https://www.acmicpc.net/problem/1039

"""
1. 덱을 사용하면 쉽게 풀리는 문제다.
2. 입력에 대해 두개씩 조합할 수 있는 경우를 구한다.
3. K번째까지 반복 후 만들 수 있는 가장 큰 수를 리턴한다. 
4. 초기 값이 0일 경우 -1 출력

"""
from collections import deque
from itertools import combinations
import sys, copy

input = sys.stdin.readline

def bfs():
    c = set()
    ans = 0
    qlen = len(q)
    while qlen:
        x = q.popleft()
        l = list(str(x))
        for i, j in d:
            s = copy.deepcopy(l)
            temp_i, temp_j = s[i], s[j]
            s[i], s[j] = temp_j, temp_i
            if s[0] == '0':
                continue
            nx = int(''.join(s))
            if nx not in c:
                ans = max(ans, nx)
                c.add(nx)
                q.append(nx)
        qlen -= 1
    return ans

n, k = map(int, input().split())
item = [i for i in range(len(str(n)))]
d = list(combinations(item, 2))
q = deque()
q.append(n)

ans = 0
while k:
    ans = bfs()
    k -= 1
if not ans:
    print(-1)
else:
    print(ans)