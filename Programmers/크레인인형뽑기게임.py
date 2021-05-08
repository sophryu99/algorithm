# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = []
    cnt = 0
    for i in moves:
        for k in range(len(board)):
            if board[k][i - 1] != 0:
                if answer:
                    if board[k][i - 1] == answer[-1]:
                        answer.pop(-1)
                        board[k][i - 1] = 0
                        cnt += 2
                    else:
                        answer.append(board[k][i - 1])
                        board[k][i - 1] = 0
                    break
                else:
                    answer.append(board[k][i - 1])
                    board[k][i - 1] = 0
                    break
            
    return cnt