# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())

for i in range(T):
    hashtb = dict() 
    lst = list(str(input()))
    for j in lst:
        hashtb[j] = hashtb.get(j,0) + 1

    res = []
    for key, value in hashtb.items():
        if value % 2 == 0:
            continue
        else:
            res.append(key)

    if len(res) == 0:
        res.append("Good")
    
    print("#{} {}".format(i+1, "".join(sorted(res))))


