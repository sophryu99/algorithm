# https://www.acmicpc.net/problem/10844

import sys

def dfs(startnum, idx):
    global count
    change = [1, -1]
    if idx == N - 1:
        count += 1
        return count

    for calc in range(2):
        newnum = startnum + change[calc] #2
        if 0 <= newnum <= 9:
            if not visited[idx + 1][newnum]:
                visited[idx + 1][newnum] = 1
                dfs(newnum, idx + 1)
                visited[idx + 1][newnum] = 0

N = int(sys.stdin.readline())

if N == 1:
    print(9)

else:
    arr = [0 for _ in range(N)]
    count = 0
    for i in range(1, 10):
        # for tracking visited numbers
        visited = [[0] * 10 for _ in range(N)]
        dfs(i, 0)
    
    print(count)










