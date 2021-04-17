# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict #1 

def solution(clothes):
    wardrobe = defaultdict(int)
    for i in clothes:
        key = i[1]	#1
        wardrobe[key] += 1 	#1
    
    count = 1
    for i in wardrobe.values():	#2
        count = count * (i + 1)
    
    return (count - 1)	#3

# 풀이: https://sophuu.tistory.com/62
