
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    DATA = list(map(int, input().split()))
    result = set()
    result.add(0)
    for i in range(N):
        temp = []
        for num in result:
            temp.append(DATA[i] + num)
        for t in temp:
            result.add(t)

    print('#{} {}'.format(test_case, len(result)))




