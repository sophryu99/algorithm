# https://www.acmicpc.net/problem/1789

"""
1. n = 1 인 경우부터 차례대로 더해서 s 보다 커지게 되면 n - 1을 리턴해준다.
2. n * (n + 1) / 2 는 1부터 n까지의 합을 구하는 공식이다.
"""
s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)

