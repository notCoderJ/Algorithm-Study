# dijkstra - simple version : Time Complexity = O(V^2) (V는 노드 수)
import sys
input = sys.stdin.readline # input을 입력에 더 효율적인 sys의 readline으로 변경

INF = int(1e9) # 10억(무한값 설정)

# 노드와 간선의 수 입력
n, e = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 각 노드별 인접 노드에 대한 거리 정보 입력
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    x, y, d = map(int, input().split()) # 노드 x -> 노드 y로 가는 거리 d
    graph[x].append((y, d))

# 최단 거리를 기록할 테이블
distance = [INF] * (n + 1)

# 방문 처리를 위한 리스트
visit = [False] * (n + 1)

# 방문하지 않은 노드 중 최단 거리의 노드를 구하는 함수
def get_shortest_node():
    min_val = INF
    shortest_node = 0
    for i in range(1, n + 1):
        if min_val > distance[i] and not visit[i]:
            min_val = distance[i]
            shortest_node = i

    return shortest_node

def dijkstra(start):
    distance[start] = 0
    visit[start] = True
    for n, d in graph[start]:
        distance[n] = d

    for _ in range(n - 1):
        current = get_shortest_node()
        visit[current] = True
        for n, d in graph[current]:
            next_dist = distance[current] + d
            if next_dist < distance[n]:
                distance[n] = next_dist

# dijkstra - fast version : Time Complexity = O(ElogV) (E는 간선 수, V는 노드 수)
# 우선 순위 큐를 지원하는 라이브러리 : PriorityQueue or heapq
# 일반적으로 heapq < PriorityQueue, heapq가 더 빠르다.
import heapq

def fast_dijkstra(start):
    distance[start] = 0

    q = [] # 우선 순위 큐
    heapq.heappush(q, (0, start))

    while q:
        dist, current = heapq.heappop(q)
        if dist > distance[current]: # 이미 처리된 노드는 무시
            continue
        for n, d in graph[current]:
            next_dist = dist + d
            if next_dist < distance[n]:
                distance[n] = next_dist
                heapq.heappush(q, (next_dist, n))

# dijkstra 수행
# dijkstra(start)
fast_dijkstra(start)

# 노드별 최단 거리 정보 출력
for i in range(1, n + 1):
    print("({}, {})".format(i, distance[i]), end=' ')

''' TEST
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
''' # (1, 0) (2, 2) (3, 3) (4, 1) (5, 2) (6, 4)