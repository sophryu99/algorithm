# https://www.acmicpc.net/problem/1032
"""
1. 첫 번째 문자열을 리스트로 저장한다.
2. For문을 돌리면서 첫 번째 문자열과 받은 문자열을 비교하여 서로 다르면 ?을 넣어준다.
"""

n = int(input())
a = list(input())
a_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))