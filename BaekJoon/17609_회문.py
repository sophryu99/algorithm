# https://www.acmicpc.net/problem/17609

"""
GREEDY algorithm
1. 회문을 확인하는 check 함수로 회문일시 0, 회문이 아닐 시 2, 유사횜문일 시 1을 출력한다.
2. 회문일 시, 유사회문을 확인하는 pseudo 함수를 재귀적으로 수행하여 유사회문을 확인한다.
"""

T = int(input())

def pseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if pseudo(word, left + 1, right) or pseudo(word, left, right - 1):
                return 1

            else:
                return 2
    return 0
            
for _ in range(T):
    word = input()
    print(check(word, 0, len(word) - 1 ))


