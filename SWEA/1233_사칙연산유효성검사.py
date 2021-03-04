# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AV185GlaI8MCFAZN#

def inorder(idx):
    if idx > N:
        return
    # if left node exists
    if (idx * 2) <= N:
        inorder(idx * 2)
    # append node value to ans
    ans.append(node[idx])
    # if right node exists
    if (idx *2 + 1) <= N:
        inorder(idx * 2 + 1)

for tc in range(10):
    N = int(input())
    node = [0] * (N+1)
    for n in range(N):
        vals = list(input().split())
        node[int(vals[0])] = vals[1]
    ans = []
    inorder(1)
    # 중외순회로 생성된 배열에서 숫자끼리의 연속이 있는지, 혹은 연산자끼리의 연속이 있는지 확인
    res = 0
    calc = ["+", "-", "/", "*"]
    for j in ans:
        if j in calc:
            res -= 1
        else:
            res += 1

    if not res == 1:
        res = 0
    
    print("#{} {}".format(tc +1, res))




