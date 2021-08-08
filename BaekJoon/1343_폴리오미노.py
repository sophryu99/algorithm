# https://www.acmicpc.net/problem/1343

"""
GREEDY algorithm
1. 보드판에서 먼저 4개의 연속 X가 있을 때 A로 채워준다.
2. 2개의 연속 X가 있을 때 B로 채워준다.
3. X가 남아있다면 -1을 리턴한다.
"""

board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)