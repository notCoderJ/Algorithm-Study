# 숨바꼭질을 하는데 1 ~ N번까지의 헛간 중 하나를 골라 숨을 수 있다.
# 술레는 항상 1번 헛간에서 출발하고 전체 맵에는 서로 다른 두 헛간을 연결하는 M개의 양방향 통로가 있다.
# 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능할 때 최단 거리가 가장 먼 헛간의 번호는?
# (최단 거리는 지나야하는 길의 최소 개수를 의미한다.)

# 풀이 전략
'''
    1번 헛간에서 최단 거리가 가장 먼 헛간을 고르기 위해서는 먼저 1번 헛간에서 출발하여
    각 헛간들에 도착하는 최단 거리를 모두 구한 후 그 중 가장 먼 헛간을 고르면 된다.
    따라서, 지정된 한 헛간(1번 헛간)에서 다른 헛간들까지의 최단 거리를 구하는 문제이므로
    다익스트라 알고리즘을 적용하여 문제를 해결할 수 있다.
    또한, 연결된 각 헛간들간의 거리가 모두 일정하므로 bfs 알고리즘으로도 해결할 수 있다.
'''

import heapq
from collections import deque

INF = int(1e9)


def dijkstra(n, path):
    distance = [INF] * (n + 1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]: # 이미 최단 거리가 정해진 헛간일 경우 무시
            continue
        for n in path[node]:
            next = dist + 1
            if next < distance[n]:
                distance[n] = next
                heapq.heappush(q, (next, n))

    max_dist = max(distance[1:])
    return distance.index(max_dist), max_dist, distance.count(max_dist)


def bfs(n, path):
    distance = [-1] * (n + 1)
    distance[1] = 0
    q = deque([1])

    while q:
        node = q.popleft()
        for n in path[node]:
            if distance[n] == -1: # 방문하지 않은 헛간인 경우 큐에 해당 헛간을 넣는다
                distance[n] = distance[node] + 1
                q.append(n)

    max_dist = max(distance)
    return distance.index(max_dist), max_dist, distance.count(max_dist)


n, m = map(int, input().split())
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

for i in dijkstra(n, path):
    print(i, end=' ')
print()

for i in bfs(n, path):
    print(i, end=' ')
print()


''' TEST
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
''' # 4 2 3


# TEST
import unittest as ut

class TestHideAndSeek(ut.TestCase):
    def test_dijkstr(self):
        n = 6
        path = [[], \
                [3, 2], \
                [3, 1, 4, 5], \
                [6, 4, 2, 1], \
                [3, 2], \
                [2], \
                [3]]
        self.assertEqual(dijkstra(n, path), (4, 2, 3))

    def test_bfs(self):
        n = 6
        path = [[], \
                [3, 2], \
                [3, 1, 4, 5], \
                [6, 4, 2, 1], \
                [3, 2], \
                [2], \
                [3]]
        self.assertEqual(bfs(n, path), (4, 2, 3))

ut.main()