# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

""" ---------- 내 풀이 (pass) ---------- """

# 접근: 이중 for문을 돌리면서 N 입력과 M 입력의 인덱스에 존재하는 값들이 일치할 때 count 증감. 
# 최종적으로 기존의 count_max 변수보다 count가 많을 시 count_max 변수 재설정

T = int(input())
for i in range(T):
    N = input()
    M = input()
    count = 0                                       # 각 인덱스의 출물 횟수를 트래킹하는 변수
    count_max = 0                                   # 출몰 횟수를 비교해서 가장 큰 횟수를 저장하는 변수
    for n in N:
        for m in M:
            if n == m:                              # M과 N의 값이 일치할 때 count 변수 증감
                count +=1
        if count > count_max or count == count_max: # count변수가 count_max의 횟수보다 크거나 같을 떄 count_max 변수 재설정
            count_max = count
        count = 0                                   # N의 다음 인덱스 탐색을 시작하기 전에 count 변수 초기화
    print('#{} {}'.format(i+1, count_max))





