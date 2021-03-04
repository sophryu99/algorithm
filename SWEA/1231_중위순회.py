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
    print("#{} {}".format(tc +1, ''.join(ans)))




