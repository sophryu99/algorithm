# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    # 먼저 리스트 정렬하기
    lst.sort(reverse = True)
    count = N
    result = []
    # 카운트를 하나씩 줄이고 홀수, 짝수 될 때마다 리스트의 앞, 뒤에서 pop 하고 새 리스트에 append하기
    for i in range(N):
        count -=1
        if count % 2 == 0:
            result.append(lst[-1])
            lst.pop(-1)
        else:
            result.append(lst[0])
            lst.pop(0)
    
    print("#{} ".format(t+1), end='')
    print(*result)
