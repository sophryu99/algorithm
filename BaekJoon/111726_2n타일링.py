N = int(input())

lst = [0, 1, 2, 3]
if N > 3:
    for i in range(4, N + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    print(lst[-1] % 100007)
else:
    print(N)