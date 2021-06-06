# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
1. divide by 2
24 -> 12 -> 6 -> 3 

2. divide by 3
24 -> 8 -> 4 -> 2 

63
1, 7, 9, 63

"""
def solution(N):
    # write your code in Python 3.6
    factors = set()
    def count(num):
        if num == 2 or num == 3 or num == 5 or num == 7:
            factors.add(1)
            return factors

        if num % 2 == 0:
            factors.add(2)
            factors.add(num // 2)
            count(num // 2)
        if num % 3 == 0:
            factors.add(3)
            factors.add(num // 3)
            count(num // 3)
        if num % 5 == 0:
            factors.add(5)
            factors.add(num // 5)
            count(num // 5)
        if num % 7 == 0:
            factors.add(7)
            factors.add(num // 7)
            count(num // 7)
        else:
            factors.add(1)
            factors.add(N)
            return factors

    count(N)
    #print(factors)
    return (len(factors))


        
