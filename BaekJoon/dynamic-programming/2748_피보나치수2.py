# https://www.acmicpc.net/problem/2748

N = int(input())

a1 = 0
a2 = 1

#       a1 a2
#    a1 a2
# a1 a2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597


count = 0
while count < N:
    temp = a2
    a2 = a1 + temp
    a1 = temp
    count +=1

print(a1)

