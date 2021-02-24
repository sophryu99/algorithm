T = int(input())

for i in range(T):
    D, L, N = map(int, input().split())
    total = D
    for j in range(1, N):
        total += D * (1 + j * L/100)
    print("#{} {}".format(i+1, int(total)))
