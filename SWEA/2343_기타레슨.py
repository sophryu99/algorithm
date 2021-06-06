# https://www.acmicpc.net/problem/2343
import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


summ = 0
for i in range(1, 10):
    summ += i

print(summ)