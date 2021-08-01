# https://www.acmicpc.net/problem/1439

"""
1. 주어진 문자열 S에서 0 -> 1 혹은 1 -> 0 으로 전환되는 지점의 인덱스를 저장해준다.
2. 저장된 지점의 리스트의 길이가 짝수일 경우, 2로 나눈 값을 출력해주고, 홀수일 경우 길이 + 1을 2로 나눈 값을 출력해준다.
"""
S = input()

idx = S[0]
points = []
for i in range(1, len(S)):
    if S[i] != idx:
        idx = S[i]
        points.append(i)

if len(points) % 2 == 0:
    print(len(points) // 2)
else:
    print ((len(points) + 1) // 2)
