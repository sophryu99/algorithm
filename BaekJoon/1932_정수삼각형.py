# https://www.acmicpc.net/problem/1932

import sys

N = int(sys.stdin.readline())
lsts = []

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    lsts.append(lst)

    # first lst
    if i == 0:
        continue
    
    # current list
    for j in range(len(lsts[i])):
        # if first element of a list
        if j == 0:
            lsts[i][j] = lsts[i][j] + lsts[i - 1][j]
        # if last element of a list
        elif j == len(lsts[i]) - 1:
            lsts[i][j] = lsts[i][j] + lsts[i - 1][j - 1]
        else:
            left = lsts[i - 1][j - 1]
            right = lsts[i - 1][j]
            # add up the bigger value
            lsts[i][j] = lsts[i][j] + max(left, right)
    
print(max(lsts[-1]))




