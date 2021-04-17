# 1번 회사에 있는 방문 판매원 A가 N개의 회사 중 K번 회사에서 소개팅 후
# X번 회사에 가서 물건을 팔 때 최단 이동 시간?
# 조건: 회사 간 통로는 양방향 이동 가능하며 이동 시간은 1

INF = int(1e9) # 무한 값 설정(10억)

# 1 -> K 와 K -> X의 최단 경로를 알아야하므로 플로이드 워셜을 이용한다.
# 방법 1 - 플로이드 워셜
def floyd_warshall(graph):
    for i in range(1, n + 1):
        for s in range(1, n + 1):
            for d in range(1, n + 1):
                graph[s][d] = min(graph[s][d], graph[s][i] + graph[i][d])

# 방법 2 - BFS
from collections import deque

def bfs(start, end, graph):
    time = [0] * (n + 1)
    q = deque([start])

    while q:
        current = q.popleft()
        # 도착 지점에 먼저 도달하면 그 시간 값을 반환
        if current == end:
            return time[current]
        for i in graph[current]:
            # start 값이 변경될 가능성이 있지만 결과 값에 영향을 주지 않음
            if time[i] == 0:
                time[i] += time[current] + 1
                q.append(i)

    return INF


# 회사 개수 n, 회사 간 경로 수 m
n, m = map(int, input().split())

# 방법 1 - 플로이드 워셜
# 최단 경로를 기록한 2차원 테이블 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에 대한 경로 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0
# 연결된 회사 정보로 2차원 테이블 갱신
for _ in range(m):
    s, d = map(int, input().split())
    graph[s][d], graph[d][s] = 1, 1
# 회사 x, k
x, k = map(int, input().split())

floyd_warshall(graph)
shortest_time = graph[1][k] + graph[k][x]

# 방법 2 - BFS
'''
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)
# 회사 x, k
x, k = map(int, input().split())

shortest_time = bfs(1, k, graph) + bfs(k, x, graph)
'''

if shortest_time < INF:
    print(shortest_time)
else:
    print(-1)

''' TEST
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
''' # 3
'''
4 2
1 3
2 4
3 4
''' # -1