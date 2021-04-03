# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 1 
end_time = meetings[0][1] 
for i in range(1, N): 
    if meetings[i][0] >= end_time: 
        cnt += 1 
        end_time = meetings[i][1] 

print(cnt)


            



            
            




