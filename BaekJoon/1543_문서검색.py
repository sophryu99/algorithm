# https://www.acmicpc.net/problem/1543

"""
GREEDY Algorithm
1. Doc 문자열 안에서 word 문자열이 존재하는지 탐색한다.
2. 존재한다면 cnt += 1, idx를 doc에서의 문자열의 마지막 idx로 재설정 해준다.
3. 존재하지 않는다면 idx만 += 1
"""

doc = input()
word = input()

idx = 0
cnt = 0

while idx < len(doc):
    if doc[idx: idx + len(word)] == word:
        cnt += 1
        idx = idx + len(word)
    else:
        idx += 1

print(cnt)


