# https://programmers.co.kr/learn/courses/30/lessons/42862

"""
Greedy 알고리즘을 사용한 접근법
- 체육복을 나눠줄 수 있는 친구의 배열과 나눔이 필요한 친구의 배열울 set으로 저장한다
- 양 옆을 확인하고 체육복을 나눔받을 수 있으면 나눔받고 불가능하다면 n에서 -1 해준다.
- 전체 n명 리턴 해주기
"""
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n-=1
    return n