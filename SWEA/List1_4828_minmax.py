T = int(input())
for i in range(T):
    a = input()
    n = list(map(int, input().split()))
    print("#{} {}".format(i+1, max(n) - min(n)))
    