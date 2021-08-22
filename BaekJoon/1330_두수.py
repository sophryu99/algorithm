# https://www.acmicpc.net/problem/1330

A,B = map(int,input().split())

print('>') if A > B else print('<') if A < B else print('==')