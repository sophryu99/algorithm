# https://programmers.co.kr/learn/courses/30/lessons/42577#

def solution(phone_book):   
    phone_book.sort()
    answer = True
    for x,y in zip(phone_book, phone_book[1:]):
        if y.startswith(x):
            answer = False
            break
    return (answer)
        
# 풀이 : https://sophuu.tistory.com/63
