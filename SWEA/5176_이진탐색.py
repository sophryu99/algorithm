# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

class Tree:
    def __init__(self, N):
        self.lst = [0] * (N + 1)
        self.N = N
        self.count = 1
        self.in_order(1)

    # 순서: left, root, right을 재귀적으로 탐색하며 숫자를 입력해준다. (in-order traversal)
    def in_order(self, num) :
        if num <= N:
            # 좌측 노드의 인덱스는 루트 노드의 두배
            # 좌측으로 계속 탐색해서 끝까지 내려감
            self.in_order(num *2)
            # root 노드 탐색
            self.lst[num] = self.count
            self.count += 1
            # 우측 노드의 인덱스는 루트 노드의 두배 + 1
            self.in_order(num * 2 + 1)
    

    def result(self):
        return ' '.join(map(str, (self.lst[1], self.lst[self.N // 2])))

T = int(input())
for tc in range(T):
    N = int(input())
    # 트리 생성, 넘버링 후 값 리턴까지
    tree = Tree(N)
    mid = tree.result
    print('#{} {}'.format(tc+1, tree.result()))
    