# https://www.acmicpc.net/problem/1946

import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    record = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    record.sort()

    minrecord = record[0][1]
    count = 1
    for i in range(1, N):
        if record[i][1] < minrecord:
            count += 1
            minrecord = record[i][1]

    print(count)


        



    