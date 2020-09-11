# N : N x N 글자판
# M: 회문의 길이

#print(word == word[::-1])

# 접근: 한 줄 안에서 M개의 길이로 존재할 수 있는 스트링을 새로운 배열에 저장해준 후 모든 배열들을 뒤집어 보고 palidrome 이 맞으면 카운트 +1

# T = int(input())
# for i in range(T):
#     N, M = map(int,input().split()) # 10, 9
#     # N번의 list를 받는다
#     hor_res = []
#     for n in range(N):
#         # 가로 먼저 탐색
#         horizontal_lst = list(input()) # GOFFAKWFSM
#         # lst 안에서 존재할 수 있는 M개의 길이를 가진 리스트를 새로운 리스트에 담아준다
#         length_M = []
#         for n in range(len(horizontal_lst)):
#             length_M.append(horizontal_lst[n: n+M-1])
#         print(length_M)
            

# lst = list(input())

# res = list()
# for i in range(len(lst)):
#     res.append(lst[i:i+3])
#     for j in range(len(res)):
#         print(reversed(res[j]))
    
# #print(res)

word = input()

print(word == reversed(word))








#print(list(word) == list(reversed(word)))