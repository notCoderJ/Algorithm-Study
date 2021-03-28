# 해당 그래프에 대해 DFS 알고리즘으로 탐색을 해보자!
# 시작 노드는 1이고 연결된 노드가 여럿일 경우 낮은 번호순으로 탐색을 진행한다.

def dfs(start, graph, visited):
    print(start, end=' ') # 방문한 노드를 출력한다.
    visited[start] = True # 현재 노드를 방문 처리한다

    for node in graph[start]:
        if not visited[node]: # 방문하지 않은 노드에 대해 dfs를 수행한다
            dfs(node, graph, visited)

# 각 노드에 연결된 노드들을 모두 순회해야 하므로
# 해당 그림의 그래프를 인접 리스트로 정의한다.
graph = [
    (), # 0번은 비워두어 노드의 값을 일치시킨다
    (2, 3, 8),
    (1, 7),
    (1, 4, 5),
    (3, 5),
    (3, 4),
    (7,), # ',' == for iterable
    (2, 6, 8),
    (1, 7)
]

# 방문 처리를 위한 리스트를 초기화한다.
visited = [False for _ in range(9)] # 0번을 고려해 9개를 생성

# 해당 그래프에 대해 dfs 시작
dfs(1, graph, visited)