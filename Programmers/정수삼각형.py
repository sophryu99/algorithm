# https://programmers.co.kr/learn/courses/30/lessons/43105


"""
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

def solution(triangle):
    
    for j in range(1, len(triangle)):
        for i in range(len(triangle[j])):
            prevlevel = triangle[j - 1]
            level = triangle[j]
            
            if i == 0:
                level[i] += prevlevel[i]
            elif i == len(level) - 1:
                level[i] += prevlevel[i - 1]
            else:
                if j == 1:
                    level[i] += prevlevel[i - 1]
                else:
                    bigger = max(prevlevel[i - 1], prevlevel[i])
                    level[i] += bigger
            
    return max(triangle[-1])
            
            
            
            

