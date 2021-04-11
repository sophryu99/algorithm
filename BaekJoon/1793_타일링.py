# https://www.acmicpc.net/problem/1793

import sys

def calc(N):
    arr = [0] * (N + 1)
    if N > 1:
        arr[0], arr[1] = 1, 1
        for i in range(2, N + 1):
            arr[i] = arr[i - 1] + 2 * arr[i - 2]
        return (arr[N])

    else:
        return 1

while True:
    try:
        print(calc(int(sys.stdin.readline())))
    except:
        break
    


