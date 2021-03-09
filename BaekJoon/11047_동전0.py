# https://www.acmicpc.net/problem/11047

# N: 동전 종류 수
# K: 만들어야 되는 액 수
N, K = map(int, input().split())
coins = []
for i in range(N):
    C = int(input())
    coins.append(C)

cnt = 0
for j in range(N - 1, -1, -1):
    if K == 0:
        break
    if coins[j] <= K:
        # 사용할 수 있는 최대의 코인 갯수
        num = K // coins[j]
        # 코인의 개수 더해주기
        cnt += num
        K = K - num * coins[j]
        
print(cnt)




