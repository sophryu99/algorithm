# 4834

T = int(input())
for i in range(1, T+1):
    size = input()
    lst = list(map(int, list(input())))
    #각 숫자 카운팅하는 변수
    numcheck = [0]*10
    #각 숫자 카운팅하기
    for t in lst:  
        numcheck[t] += 1
    #숫자와 횟수
    index = 0
    maxnum = 0
    #반복문
    for j in range(9, 0, -1):
        if numcheck[j] > maxnum :
            maxnum = numcheck[j]
            index = j
    #출력
    print("#{} {} {}".format(i, index, maxnum))