# 메시지를 전송할 수 있는 통로가 설치된 N개의 도시 중 C라는 도시에서 메시지를 보낼 때
# 메시지를 받는 도시의 개수와 모두 메시지를 받는 데까지 걸리는 시간?
# 조건:
#   X -> Y로 통로가 있으면 X는 Y로 메시지를 전송 가능하지만 Y -> X가 없으면 반대는 불가능

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


# 도시 개수 n, 통로 개수 m, 메시지 전송 도시 c
n, m, c = map(int, input().split())
# 도시 연결 정보를 위한 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

time = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[c] = 0

    while q:
        time_val, current = heapq.heappop(q)
        if time[current] < time_val: # 현재 시간 값이 더 작으면 이미 갱신되었으므로 무시
            continue
        else:
            for n, t in graph[current]:
                next = time_val + t
                if time[n] > next:
                    time[n] = next
                    heapq.heappush(q, (next, n))

dijkstra(c)

city_cnt = -1 # 시작 노드 제외를 위해 -1로 시작
max_time = -1
for i in time:
    if i == INF:
        continue
    city_cnt += 1
    max_time = max(max_time, i)

print(city_cnt, max_time)

''' TEST
3 2 1
1 2 4
1 3 2
''' # 2 4