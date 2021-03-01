
def bfs(v):
    # 노드 번호만 넣는 큐
    q = []
    q.append(v)
    # 방문표시
    visited[v] = 1
    while q:
        # 방향이 따로 없으니 이어져 있는 노드 모두 탐색
        # 첫번째 원소부터 탐색
        v = q.pop(0)
        for e in range(E):
            # 앞 먼저 탐색
            # 탐색하는 노드와 그에 이어져 있는 간선을 방문하지 않은 경우
            if node[e][0] == v and visited[node[e][1]] == 0:
                # 다음 탐색을 위해 v 와 이어져 있는 간선 q에 append
                q.append(node[e][1])
                # 다음 노드 방문 표시
                visited[node[e][1]] = 1
                distance[node[e][1]] = distance[v] + 1
            if node[e][1] == v and visited[node[e][0]] == 0:
                # 다음 탐색을 위해 v 와 이어져 있는 간선 q에 append
                q.append(node[e][0])
                visited[node[e][0]] = 1
                distance[node[e][0]] = distance[v] + 1


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    bfs(S)
    print("#{} {}".format(tc+1, distance[G]))


   
