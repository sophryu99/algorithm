# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

T = int(input())
ans = list()

for i in range(1, T+1):
    i = str(i)
    lst = ["3", "6", "9"]
    if "3" in i or "6" in i or "9" in i:
        num = ""
        for j in range(len(i)):
            if i[j] == "3" or i[j] == "6" or i[j] == "9":
                num += "-"
        ans.append(num)
    else:
        ans.append(i)

print(" ".join(ans))
