T = int(input())

for i in range(T):
    word = input()
    res = 0
    if word == word[::-1]:
        res = 1
    else:
        res = 0
    print("#{} {}".format(i+1, res))
