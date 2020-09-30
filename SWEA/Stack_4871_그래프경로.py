# [문제]
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
# 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
# E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


""" ---------- 내 풀이 (pass) ---------- """

# 접근: 노드 값들을 각각 딕셔너리에 저장해준다. 출발 노드와 마지막 노드를 입력 값으로 받고 출발 노드에서 이어지는 노드를 깊이 우선 탐색으로 탐색하고 마지막 노드와 일치하면 1 리턴

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
    
