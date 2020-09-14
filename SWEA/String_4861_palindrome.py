# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# N : N x N 글자판
# M: 회문의 길이

""" ---------- 내 풀이 () ---------- """

# 접근: 한 줄 안에서 M개의 길이로 존재할 수 있는 스트링을 새로운 배열에 저장해준 후 모든 배열들을 뒤집어 보고 palidrome 이 맞으면 해당 string 값을 리턴한다
# 가로 후 세로 순서로 진행한다

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    horizontal_res = []                        
    for n in range(N):
        lst_h = input()                         # 1. 가로 먼저 탐색
        result_h = []                           # 입력받는 리스트 N에서 M개의 길이인 스트링값 저장하는 변수
        for m in range(len(lst_h)):
            result_h.append(lst_h[m:m+M])       # 입력받는 리스트 범위 내에서 M의 길이만큼의 배열을 result_h에 저장한다
        for r in result_h:
            if len(r) == M:                     # result_h에서 길이가 M이고
                if r == r[::-1]:                # 뒤집었을 때 원래의 값과 같은 값에 한해서
                    horizontal_res.append(r)    # horizontal_res에 저장해준다.
    
    vertical_res = []                           # 2. 세로 탐색 시작
    vertical_list = []                          # N번 입력 리스트를 받으며 새로 생성하는 리스트 변수
    for x in range(N):
        lst_v = input()
        vertical_list.append(lst_v[x])
    





        
