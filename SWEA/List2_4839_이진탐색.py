# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

# 이진탐색 함수 만들기
# p = 전체 쪽수, l = 첫째 쪽수, a = 찾아야하는 쪽수, count = 이진탐색 실시 횟수
def binarySearch(p, l, a, count):
    c = int((l+p)/2)
    # 최종 변수
    result = count
    if a == c:
        print(int(result))
        return(int(result))
    # a가 중간값보다 큰 경우 l = c
    elif a > c:
        binarySearch(p, c, a, count+1)
    # a가 중간값보다 작은 경우 p = c
    elif a < c:
        binarySearch(c, l, a, count+1)
    else:
        return -1
    return count

T = int(input())
for t in range(T):
    P, A, B = map(int,input().split())
    a_res = binarySearch(P, 1, A, 0)
    b_res = binarySearch(P, 1, B, 0)
    print(a_res,b_res)
    if a_res > b_res:
        print('A')
    elif a_res < b_res:
        print('B')
    else:
        print(0)
