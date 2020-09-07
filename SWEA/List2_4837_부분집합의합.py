# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# combination 라이브러리 사용
from itertools import combinations

lst = [1,2,3,4,5,6,7,8,9,10,11,12]

# 함수 생성
def createCombination(a, n, k):
    sets = []
    # 우선 리스트에 대한 부분집합 모두 생성
    for i in range(0, len(a)+1):
        c = combinations(a, i)
        sets.extend(c)
    # 해당 부분집합 안에 길이가 N인 부분집합만 새로운 리스트에 추가
    set_length = []
    for j in sets:
        if len(j) == n:
            set_length.append(j)
    # 해당 길이의 부분집합 중 합이 K인 부분집합만 새로운 리스트에 추가
    set_result = []
    for s in set_length:
        if sum(s) == k:
            set_result.append(s)
    return(len(set_result))    


T = int(input())
for t in range(T):
    result = []
    N, K = map(int,input().split())
    print("#{} ".format(t+1), end='')
    print(createCombination(lst, N, K))


