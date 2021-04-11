# https://www.acmicpc.net/problem/2407

"""
nCr = n! / r!(n - r)!
"""

import sys

N, R = map(int, sys.stdin.readline().split())

def dp(num):
    arr = {}
    if num in arr:
        return arr[num]
    elif num == 0 or num == 1:
        arr[num] = 1
        return 1
    else:
        factorial = num * dp(num - 1)
        arr[num] = factorial
    return factorial

ans = dp(N) // (dp(R) * dp(N - R))
print(ans)