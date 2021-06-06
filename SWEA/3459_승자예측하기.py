# D4
# 뒤에서부터 빼가며 카운트가 홀수 일때는 밥의 승, 짝수일때는 앨리스의 승

# [0, 0, 0, 0, 0, 5]
"""
5
1. - 2x = 3
2. - 2x + 1 = 2

"""

def play(num, cnt):
    
    if num > N:
        print(cnt)
        return

    # 2x + 1, 2x로 뺀 결과에 대해 재귀적으로 수행
    return play(2 * num, cnt + 1) and \
         play(2 * num + 1, cnt + 1)
    

T = int(input())

for tc in range(T):
    N = int(input())
    play(1, 1)


