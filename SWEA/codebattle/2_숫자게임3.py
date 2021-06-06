
T = int(input())

for tc in range(T):
    N = str(input())
    maxnum = 0
    q = []
    q.append((1, N, 0))
    
    while q:
        newnum, num, cnt = q.pop(0)
        # print('q', newnum, num, cnt)

        if len(num) == 1:
            if cnt > maxnum:
                maxnum = cnt
        # if len(N) == 5:
        #     break

        for i in range(1, len(num)):
            res = newnum * int(num[0 : i]) * int(num[i : len(num)])
            q.append((1, str(res), cnt + 1))

            if len(num[i : len(num)]) >= 2:
                q.append((int((num[0 : i])), num[i : len(num)], cnt + 1))

    print("#{} {}".format(tc + 1, maxnum))
