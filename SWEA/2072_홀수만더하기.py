T = int(input())

for i in range(T):
    lst = list(map(int, input().split()))
    oddsum = 0
    for j in range(len(lst)):
        if lst[j] % 2 == 1:
            oddsum += lst[j]
    print("#{} {}".format(i+1, oddsum))

