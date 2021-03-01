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