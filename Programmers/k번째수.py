# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3


def solution(array, commands):
    # i, j, kth
    answer = []
    for i in commands:
        newarr = sorted(array[i[0] - 1 : i[1]])
        answer.append(newarr[i[2]-1])
    return answer

