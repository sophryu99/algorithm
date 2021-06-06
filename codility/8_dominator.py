# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    # dominator: value that occurs more than half of the elements of A
    diction = defaultdict(int)

    for i in range(len(A)):
        diction[A[i]] += 1
        if diction[A[i]] > len(A) // 2:
            return A.index(A[i])
    
    return -1


"""
100 %
ON log N or ON 
"""