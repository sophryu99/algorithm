# https://www.acmicpc.net/problem/12865
# import sys

# N, K = map(int, sys.stdin.readline().split())

# lst = []
# for _ in range(N):
#     items= list(map(int, sys.stdin.readline().split()))
#     lst.append(items)

# maxsum = 0
# for i in range(N):
#     weight = K
#     localsum = 0
#     while weight >= 0:
#         for j in range(i, N):
#             if lst[j][0] <= weight:
#                 weight -= lst[j][0]
#                 #print('w', weight)
#                 localsum += lst[j][1]
#         break
    
#     if localsum > maxsum:
#         maxsum = localsum
#         #print('m', maxsum)

# print(maxsum)
            
import sys

r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])




