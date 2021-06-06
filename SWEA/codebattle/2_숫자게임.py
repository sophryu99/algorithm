def calc(num, cnt, numprev):
    global maxnum
    # 한자리 숫자가 됐을 시
    if len(str(num)) == 1:
        if cnt > maxnum:
            maxnum = cnt
        #print("cnt", num, cnt)
        return int(num)

    # if len(num) == 5:
    #     return 0

    for i in range(1, len(num)):
        # 앞부분과 뒷부분을 순차적으로 쪼갰을 때 곱한 결과로 재귀적 수행
        newnum = int(num[0 : i]) * int(num[i : len(num)]) * numprev  # 2, 43 -> 86 | 8, 6 -> 48 | 4, 8 -> 32 | 3, 2 -> 6
        #print("new", newnum)
        if len(num) > 2:
            # 앞부분은 유지하되 뒷부분을 순차적으로 쪼갰을 때 곱한 결과로 재귀적 수행
            calc(str(num[i: len(num)]), cnt + 1, int(num[0:i])) # 2, "43" (4, 3 -> 12 | 1, 2 -> 2)
        calc(str(newnum), cnt + 1, 1)

    return
    

T = int(input())

for tc in range(T):
    N = input()
    maxnum = 0
    calc(str(N), 0, 1)
    print("#{} {}".format(tc + 1, maxnum))
