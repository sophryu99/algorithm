N = int(input())

dp = [1, 1, 2]

N = N - 1
if N > 2:
    for i in range(3, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp[N])

else:
    print(dp[N])