# 위상 정렬 알고리즘

from collections import deque


# 노드와 간선 수 입력
v, e = map(int, input().split())

def topology_sort(graph, indegree):
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur_node = q.popleft()
        print(cur_node, end=' ')
        for i in graph[cur_node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


# 진입차수 초기화
indegree = [0] * (v + 1)

# 각 노드의 연결된 간선 정보를 저장하기 위한 그래프 초기화
graph = [[] for _ in range(v + 1)]

# 간선 정보 입력 및 진입차수 설정
for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1

# 위상 정렬 수행
topology_sort(graph, indegree)


''' TEST
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
''' # 1 2 5 3 6 4 7