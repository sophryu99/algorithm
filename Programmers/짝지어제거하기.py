# https://programmers.co.kr/learn/courses/30/lessons/12973
# https://sophuu.tistory.com/82

def solution(s):
    q = []
    idx = 0
    while idx < len(s):
        letter = s[idx]
        if not q:
            q.append(letter)
        elif q[-1] == letter:
            q.pop()
        else:
            q.append(letter)
        idx += 1
            
    if q:
        return 0
    else:
        return 1