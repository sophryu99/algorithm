# 다시 풀어보기!
# https://www.acmicpc.net/problem/2193

N = int(input())
 
dp = [0 for _ in range(91)]                # 0으로 이루어져 있는 92개의 빈 배열 생성
 
for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]
 
print(dp[N])