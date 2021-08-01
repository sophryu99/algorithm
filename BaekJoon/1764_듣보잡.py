# https://www.acmicpc.net/problem/1764
"""
1. 들어본 사람, 본 사람 리스트를 각각 받아준다.
2. 두 리스트의 교집합을 구해준다.
3. 리스트를 오름차순으로 정렬해주고, 리스트의 길이와 각 원소를 출력해준다.
"""
import sys

N, M = map(int, sys.stdin.readline().split())
heard = [input() for _ in range(N)]
seen = [input() for _ in range(M)]

diction = set(heard).intersection(set(seen))
lst = list(diction)
lst.sort()
print(len(lst))
for name in lst:
    print(name)


