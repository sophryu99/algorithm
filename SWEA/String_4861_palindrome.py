# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# N : N x N 글자판
# M: 회문의 길이

""" ---------- 내 풀이 (pass) ---------- """

# 접근: 한 줄 안에서 M개의 길이로 존재할 수 있는 스트링을 새로운 배열에 저장해준 후 모든 배열들을 뒤집어 보고 palidrome 이 맞으면 해당 string 값을 리턴한다
# 가로 후 세로 순서로 진행한다
# 수정: 원래 가로 후 세로 순서로 진행하려 했으나, N개의 리스트 입력값을 받을 때 따로따로 하게 되면 input을 두번 넣어야한다. 따라서 한 번의 for loop 안에 가로, 세로 리스트 둘 다 처리할 것

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    final_res = []                                  # 최종 출력 값

    vertical_list = []                        
    for n in range(N):
        lst_h = input()                             # 1. 가로 먼저 탐색
        result_h = []                               # 입력받는 리스트 N에서 M개의 길이인 스트링값 저장하는 변수
                                                    # 2. 세로 탐색 같이 진행
        lst_v = list(map(str, lst_h))               # N번 리스트 입력 값을 받고            
        vertical_list.append(lst_v)                 # 새로운 변수에 해당 입력 값을 저장해준 후 for문이 끝난 후 -- 세로 탐색 여기까지
        for m in range(len(lst_h)):
            result_h.append(lst_h[m:m+M])           # 입력받는 리스트 범위 내에서 M의 길이만큼의 배열을 result_h에 저장한다
        for r in result_h:
            if len(r) == M:                         # result_h에서 길이가 M이고
                if r == r[::-1]:                    # 뒤집었을 때 원래의 값과 같은 값에 한해서
                    final_res.append(r)             # horizontal_res에 저장해준다.
    temp = [list(x) for x in zip(*vertical_list)]   # # 전치 시켜준다 (행과 열을 반전 시켜준다) -- 세로 탐색 다시 시작
    transposed = []                             
    for j in temp:
        transposed.append(''.join(j))               # 전치 시켜준 각 행을 join 시켜서 transposed 리스트에 저장

    temp_result = []
    vertical_res = []
    for t in transposed:                            # transposed 리스트 내의 element 값을 탐색하며 
        for m2 in range(len(t)):
            temp_result.append(t[m2:m2+M])          # temp_result에 저장해준다
        for r2 in temp_result:
            if len(r2) == M:                        # temp_result에 길이가 M이고
                if r2 == r2[::-1]:                  # 뒤집었을 때 원래의 값과 같은 값에 한해서
                    final_res.append(r2)            # vertical_res에 저장해준다.
    print('#{} {}'.format(i+1, final_res[0]))





        
