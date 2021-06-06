# https://www.acmicpc.net/problem/2475

"""
1. 각 숫자들의 제곱을 더한다.
2. 더한 결과를 10으로 나눈 나머지를 출력한다."""

import sys
nums = list(map(int, sys.stdin.readline().split()))

summ = 0

for i in nums:
    summ += i**2

print(summ % 10)