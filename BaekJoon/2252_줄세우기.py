# https://www.acmicpc.net/problem/2252

"""
1. 학생들의 키 정보를 그래프로 생성한다.
2. 덱을 사용해서 풀었다.
3. 위상 정렬을 진행해준다.
"""

import collections

v, e = map(int, input().split())
in_degree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1
    
result = []
q = collections.deque()

for i in range(1, v+1):
    if in_degree[i] == 0:
        q.append(i)
        
while q:
    node = q.popleft()
    result.append(node)
    
    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')