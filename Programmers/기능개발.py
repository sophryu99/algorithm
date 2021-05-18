# https://programmers.co.kr/learn/courses/30/lessons/42586
# https://sophuu.tistory.com/83

import math

def solution(progresses, speeds):
    # progress: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 배열
    # speed: 개발 속도
    # 각 배포마다 몇개의 기능이 배포되는지
    order = []
    for i in range(len(progresses)):
        total = 100 - progresses[i]
        days = math.ceil(total / speeds[i])
        order.append(days)
        
    # two pointer
    result = [1]
    for j in range(len(order) - 1):
        if order[j] >= order[j + 1]:
            order[j + 1] = order[j]
            result[-1] += 1
        else:
            result.append(0)
            result[-1] += 1
    
    return result