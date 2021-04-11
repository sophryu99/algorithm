# https://www.acmicpc.net/problem/9658

import sys

N = int(sys.stdin.readline())

def solution(n):
    dp = [0] * (n + 5)
    dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1

    for i in range(5, n + 1):
        if dp[i - 1] and dp[i - 3] and dp[i - 4]:
            dp[i] = 0
        else:
            dp[i] = 1

    if dp[n] == 1:
        print('SK')
    else:
        print('CY')
    return dp[-1]

solution(N)