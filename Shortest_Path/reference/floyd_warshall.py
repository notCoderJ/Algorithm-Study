# floyd warshall : Time Complexity = O(v³) (V는 노드 수)

INF = int(1e9) # 무한 값 설정(10억)

def floyd_warshall(graph):
    for i in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][i] + graph[i][y])

# 노드 수와 간선 수를 입력받음
n, e = map(int, input().split())
# 모든 노드 간 최단 경로를 기록할 2차원 테이블 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신 경로 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0
# 최단 경로 테이블을 입력받은 인접 노드 정보로 초기화
for _ in range(e):
    x, y, d = map(int, input().split())
    graph[x][y] = d

# 플로이드 워셜 수행
floyd_warshall(graph)

print("--------")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

''' TEST
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
''' # 0 4 8 6
    # 3 0 7 9
    # 5 9 0 4
    # 7 11 2 0