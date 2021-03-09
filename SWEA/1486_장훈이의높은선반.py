from itertools import combinations

T=int(input())

for test in range(1,T+1):
    N, Height = map(int,input().split())
    heightlist = list(map(int,input().split()))
    heights=set()
    heightlist.sort()
    tempmin=99999
    for i in range(1,N+1):
        combs = list(combinations(heightlist,r=i))
        for j in combs:
            heights.add(sum(j))
    if Height in heights:
        answer = 0
    else : 
        for i in heights:
            if 0< i-Height < tempmin:
                tempmin=i-Height
        answer = tempmin
    print('#{} {}'.format(test, answer))