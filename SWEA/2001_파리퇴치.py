T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]
    maxsum = 0
    for k in range(N - M + 1):
        for j in range(N - M + 1):
            curr = 0
            for l in range(M):
                for m in range(M):
                    curr += square[l+k][m+j]
            
            if curr > maxsum:
                maxsum = curr

    print("#{} {}".format(i+1, maxsum))

