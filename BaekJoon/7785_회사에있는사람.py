T = int(input())

record = {}
for i in range(T):
    person, action = map(str, input().split())
    record[person] = action                         # dictionary에 해당 사람의 status를 update 해준다

names = []
for key, val in record.items():                     # status가 enter인 사람들만 출력
    if val == 'enter':
        names.append(key)

names.sort(reverse = True)                          # 알파벳 역순으로 이름 출력
for i in names:
    print(i)