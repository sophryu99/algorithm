# https://programmers.co.kr/learn/courses/30/lessons/17677#


def solution(str1, str2):
    str1, str2 = list(str1.lower()), list(str2.lower())
    common = 0
    added = 0
    
    def create(lst):
        sets = []
        for i in range(len(lst) - 1):
            sample = lst[i: i + 2]
            if ''.join(lst[i: i + 2]).isalpha():
                sets.append(lst[i: i + 2])
        return sets
    
    sets1 = create(str1)
    sets2 = create(str2)
    minn, maxx = sets1, sets2
    
    
    if len(sets1) != len(sets2):
        minn = min(sets1, sets2)
        maxx = max(sets1, sets2)
    
    lenminn, lenmaxx = len(minn), len(maxx)
    
    for s in range(len(minn)):
        if minn[s] in maxx:
            common += 1
            maxx.remove(minn[s])
            
    if lenminn == 0 and lenmaxx == 0:
        return 65536
    else: 
        return int(common * 65536 / (lenminn + lenmaxx - common))