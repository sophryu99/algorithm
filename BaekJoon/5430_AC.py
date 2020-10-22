
T = int(input())

prompt = []
for i in range(T):
    a = list(input())
    N = int(input())
    lst = input()
    B = list()
    for cmd in range(len(a)):
        if a[cmd] == 'R':
            B.append(lst[::-1])
        #elif a[cmd] == 'D':

