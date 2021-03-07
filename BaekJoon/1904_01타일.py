# https://www.acmicpc.net/problem/1904
"""
N = 1 -> 1
N = 2 -> 00
N = 3 -> 001, 100, 111
N = 4 -> 0011, 0000, 1001, 1100, 1111
N = 5 -> 00111, 00001, 00100, 10011, 10000, 11001, 11100, 11111
.
.
.
fibonacci - solve by memoization
"""

lst = [0, 1, 2]

N = int(input())

for i in range(3, N+1):
    lst.append((lst[i-2] + lst[i-1]) % 15746)

print(lst[N])
