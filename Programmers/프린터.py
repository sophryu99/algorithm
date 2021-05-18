# https://programmers.co.kr/learn/courses/30/lessons/42587#

def solution(priorities, location):
    cnt = 0
    start = 0
    current_location = location
    while len(priorities) > 0:
        if len(priorities) == 1:
            return cnt + 1
        
        if priorities[start] < max(priorities[start + 1: len(priorities) + 1]):
            priorities.append(priorities[start])
            priorities.pop(start)
            if current_location == 0:
                current_location = len(priorities) - 1
            else:
                current_location -= 1
        else:
            priorities.pop(start)
            cnt += 1
            if current_location == 0:
                break
            else:
                current_location -= 1
            
    return cnt