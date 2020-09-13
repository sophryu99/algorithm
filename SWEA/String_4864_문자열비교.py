# [입력]

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

""" ---------- 내 풀이 (pass) ---------- """
# 접근: M안에서 존재할 수 있는 N의 길이와 같은 문자열을 모두 출력하여 저장한 후, N과 비교해서 일치하면 1 리턴.

T = int(input())
for i in range(T):
    N = input()
    M = input() 
    result = []
    count = 0
    for l in range(len(M)):             # M입력 길이 안에서의 인덱스 각각 비교
        result.append(M[l:l+len(N)])    # N입력의 길이만큼 존재하는 String 배열 result에 저장
    for m in result:                    # result list에서
        if m == N:                      # 입력 N의 스트링 값과 값이 일치하면
            count +=1                   # count 증감
    print("#%d %d" %(i+1,count))

    
    

