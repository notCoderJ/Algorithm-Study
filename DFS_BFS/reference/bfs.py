# 해당 그래프에 대해 BFS 알고리즘으로 탐색을 해보자!
# 시작 노드는 1이고 연결된 노드가 여럿일 경우 낮은 번호순으로 탐색을 진행한다.

# 큐를 사용하기 위해 collections 모듈의 deque 자료구조를 활용하자!
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start]) # BFS를 위해 시작 노드가 들어있는 큐를 생성한다
    visited[start] = True # 시작 노드를 방문 처리한다

    while queue:
        front = queue.popleft() # 큐에서 노드를 꺼내
        print(front, end=' ')
        for node in graph[front]: # 인접한 노드 중 방문하지 않은 모든 노드를 큐에 넣는다.
            if not visited[node]:
                queue.append(node)
                visited[node] = True

# 각 노드에 연결된 노드들을 모두 순회해야 하므로
# 해당 그림의 그래프를 인접 리스트로 정의한다.
graph = [
    (), # 0번은 비워두어 노드의 값을 일치시킨다
    (2, 3, 8),
    (1, 7),
    (1, 4, 5),
    (3, 5),
    (3, 4),
    (6,),
    (2, 6, 8),
    (1, 7)
]

# 방문 처리를 위한 리스트를 초기화한다.
visited = [False] * 9 # 1차원 리스트를 초기화하는 또다른 방법

# 해당 그래프에 대해 bfs 시작
bfs(1, graph, visited)