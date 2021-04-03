# https://www.acmicpc.net/problem/16953

import sys

def bfs(num, B):
    q = []
    q.append((num, 0))

    while q:
        newnum, count = q.pop(0)
        calcnums = [(lambda x: x * 2)(newnum), int((lambda x: x + '1')(str(newnum)))]
        for i in calcnums:
            if i > B:
                break
            elif i not in visited:
                visited.append(i)
                q.append((i, count + 1))
                print(visited)
                print(i, count)
                if i == B:
                    return (count + 2)
    
    return -1

A, B = map(int, sys.stdin.readline().split())
visited = []
print(bfs(A, B))



# print((lambda x: x * 2)(A), int((lambda x: x + '1')(str(A))))

