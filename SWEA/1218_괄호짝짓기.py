for tc in range(10):
    N = int(input())
    lst = list(map(str, input()))
    stck = list()

    # 왼쪽 괄호
    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']
    for i in range(N):
        if lst[i] in left:
            stck.append(lst[i])
            #print(stck)
        if lst[i] in right:
            # 가장 상위의 괄호 값과 쌍이라면
            if right.index(lst[i]) == left.index(stck[-1]):
                # 상위의 원소 제거하기
                stck.pop()
                #print(stck)
            else:
                break
                
    res = 0
    if len(stck) == 0:
        res = 1
    
    print("#{} {}".format(tc + 1, res))


