# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg


def node_num(root):
    global cnt 
    
    node = [root]
    while node:
        rt = node.pop()
        if left[rt]:
            node.append(left[rt]) 
            # should uncomment
            #cnt +=1 
        if right[rt]:
            node.append(right[rt])
            # should uncomment
            #cnt +=1

T = int(input())

for tc in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 1

    # 루트에 자식 추가할 array 만들어주기
    left = [0]*(E+2) # 첫번째 자식
    right = [0]*(E+2) # 두번째 자식

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        # 왼쪽 노드에 이미 값이 존재한다면 오른쪽 노드에 저장
        if left[parent]:
            right[parent] = child
        # 왼쪽 노드에 자식 노드가 없을 시 왼쪽 노드에 저장
        else:
            left[parent] = child
    
    node_num(N)
    print("#{} {}".format(tc + 1, cnt))
