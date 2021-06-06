# https://www.acmicpc.net/problem/18114

import sys

N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

count = 0
midsum = 0
end = 1

for i in range(N):
    nextidx = i + 1
    for nextidx in range(N - 1):
        print(i, nextidx)





