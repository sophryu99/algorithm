# https://www.acmicpc.net/problem/14501

"""
totaldays = N + 1
today = 0
while totaldays > 0:
    days = time[today]
    money = price[today]
    today = today + days
    meeting[today] = money
    totaldays = totaldays - today
print(meeting)
"""


"""
뒤에서부터 접근해보자
max_pay[i] = max(pay + max_pay[i + day], max_pay[i+1])
"""

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])

    