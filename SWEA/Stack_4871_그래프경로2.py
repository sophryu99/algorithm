def dfs(lst, start, end):
    visited = []                                # 방문한 노드 저장하는 리스트
    stk = []                                    # 탐색하는 노드 저장하는 스택
    stk.append(start)                           # 시작 노드를 스택에 저장
    while stk:                                  # 스택 안에 노드가 존재할 때
        node = stk.pop()                        # node 변수에 스택 안의 노드를 pop 하고 저장
        print(node)
        if node not in visited:                 # node가 이미 탐색 된 node가 아닐 때
            visited.append(node)                # visited에 넣어줌
            stk += lst[node]                   # stack에 node에 연결된 다음 노드들을 append 해준다
    if end in visited:
        return 1
    else :
        return 0

T = int(input())
for t in range(T):
    V, E = map(int, input().split())            # 노드 개수, 간선 개수 입력 받기
    diction = {1 : set([])}                     # 딕셔너리 생성
    for j in range(2, V+1):                     # 노드 개수만큼 딕셔너리 생성
        diction[j] = set([])
    for i in range(E):                          # 입력 값을 각각 딕셔너리에 맞게 add 해준다
        start, end = map(int,input().split())
        diction[start].add(end)
    print(diction)

    A, B = map(int, input().split())            # 시작 노드, 끝 노드 입력 받기
    print("#{} {}".format(t+1, dfs(diction, A, B)))