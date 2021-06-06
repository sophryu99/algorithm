N = int(input())
cnt = 0

while N >= 4:
    # N이 3의 제곱보다 크거나 같다면
    if N >= 3 * 3:
        N = N - 3 * 3
        cnt += 1
        
    # N이 2의 제곱보다 크고 3의 제곱보다 작다면
    else:
        N = N - 2 * 2
        cnt += 1

lst = [0, 1, 2, 3]   
cnt += lst[N] 

print(cnt)




