# 1 ~ N번의 도시와 M개의 단방향 도로가 있는 나라가 있을 때, 특정한 도시 X에서 출발하여
# 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시의 번호를 출력하시오.
# (단, 모든 도로의 거리는 1입니다.)

from collections import deque

def bfs(start, graph, path_table):
    q = deque([start])
    path_table[start] = 0 # 시작 지점의 거리는 0으로 초기화

    while q:
        current = q.popleft()
        for i in graph[current]:
            if path_table[i] == -1:
                path_table[i] = path_table[current] + 1
                q.append(i)

    exist = False
    for i in range(1, n + 1):
        shortest_path = path_table[i]
        if shortest_path == k:
            exist = True
            print(i)

    if not exist:
        print(-1)


n, m, k, x = map(int, input().split())

# 단방향 도로 정보를 기록할 그래프 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# 최단 경로 테이블 초기화
path_table = [-1] * (n + 1)

bfs(x, graph, path_table)


''' TEST
4 4 2 1
1 2 
1 3
2 3
2 4
''' # 4