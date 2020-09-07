T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    answer = []
    for j in range(N-M+1):
        answer.append(sum(a[j:j+M]))
    print("#{} {}".format(i,(max(answer)-min(answer))))