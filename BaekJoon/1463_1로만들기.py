N = int(input())

if N % 2 == 0:
    N = N // 2
elif N % 3 == 0:
    N = N // 3
else:
    N -= 1