T = int(input())

for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    currmax = lst[0]
    ans = 0

    for j in range(N):
        if currmax > lst[j]:
            ans += currmax - lst[j]
        else:
            currmax = lst[j]
    
    print("#{} {}".format(i + 1, ans))
    
