
# def fib(N):
#     global count_one, count_zero
#     if N == 1:
#         count_one += 1
#         return 1
#     elif N == 0:
#         count_zero += 1
#         return 0
#     else:
#         return (fib(N-1) + fib(N-2))

# T = int(input())

# for tc in range(T):
#     N = int(input())
#     count_one = 0
#     count_zero = 0

#     fib(N)
#     print(count_zero, count_one)


# N이 0, 1 일때의 0과 1의 출현 빈도수
cnt0 = [1, 0]
cnt1 = [0, 1]

# t번의 테스트 케이스에서 같은 결과물을 사용할 것이기 때문에 N의 최대 수까지 계산을 해놓는다.
for i in range(2, 41):
    cnt0.append(cnt0[i-1]+cnt0[i-2])
    cnt1.append(cnt1[i-1]+cnt1[i-2])

for _ in range(int(input())):
    n = int(input())
    print(cnt0[n], cnt1[n])