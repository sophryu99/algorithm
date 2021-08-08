# https://www.acmicpc.net/problem/1157

"""
1. 문자열을 모두 대문자로 치환한 후 탐색하여 최다 빈도 알파벳을 리턴한다.
2. 두 개 이상이라면 ?을 리턴한다.

"""
from collections import defaultdict
word = input().upper()

d = defaultdict(int)

for i in word:
    d[i] += 1

max_keys = [k for k, v in d.items() if v == max(d.values())]
if len(max_keys) == 1:
    print(max_keys[0])
else:
    print('?')