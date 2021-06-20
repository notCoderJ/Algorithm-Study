# 화성 탐사 기계의 에너지를 효율적으로 사용하고자 출발 지점에서 목표 지점까지 이동할 때
# 최적의 경로로 이동해야 한다. 기계는 N * N 크기의 2차원 공간에 있고 상하좌우 인접한 곳으로
# 1칸씩 이동할 수 있으며, 각 칸을 이동하는데는 에너지가 소모된다. 출발 지점 [0][0]에서
# 목표 지점 [N-1][N-1]까지 이동할 때 최소 비용은?

#풀이 전략
'''
    칸마다 '에너지 소모량이 다른' 2차원 공간에서
    '한 지점(출발점)에서 다른 한 지점(목표점)으로 이동할 때 최소 비용'을 구하는 문제이므로
    주어진 2차원 공간에 다익스트라 알고리즘을 적용하면 해결할 수 있다.
'''

import heapq

INF = int(1e9)


def dijkstra(n, costs):
    spend = [[INF] * n for _ in range(n)]
    spend[0][0] = costs[0][0]
    q = []
    heapq.heappush(q, (spend[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)
        if cost > spend[x][y]: # 이전 소비 비용이 더 작다면 무시
            continue
        else:
            if x > 0: # 현지점에서 윗 방향에 대한 에너지 소모량을 계산한다
                up = cost + costs[x - 1][y]
                if up < spend[x - 1][y]:
                    spend[x - 1][y] = up
                    heapq.heappush(q, (up, x - 1, y))
            if x < n - 1: # 현지점에서 아랫 방향에 대한 에너지 소모량을 계산한다
                down = cost + costs[x + 1][y]
                if down < spend[x + 1][y]:
                    spend[x + 1][y] = down
                    heapq.heappush(q, (down, x + 1, y))
            if y > 0: # 현지점에서 좌측 방향에 대한 에너지 소모량을 계산한다
                left = cost + costs[x][y - 1]
                if left < spend[x][y - 1]:
                    spend[x][y - 1] = left
                    heapq.heappush(q, (left, x, y - 1))
            if y < n - 1: # 현지점에서 우측 방향에 대한 에너지 소모량을 계산한다
                right = cost + costs[x][y + 1]
                if right < spend[x][y + 1]:
                    spend[x][y + 1] = right
                    heapq.heappush(q, (right, x, y + 1))

    return spend[n - 1][n - 1]


def dijkstra_v2(n, costs):
    spend = [[INF] * n for _ in range(n)]
    spend[0][0] = costs[0][0]
    q = []
    heapq.heappush(q, (spend[0][0], 0, 0))
    mv = ((-1, 0), (1, 0), (0, -1), (0, 1)) # up down left right

    while q:
        cost, x, y = heapq.heappop(q)
        if cost > spend[x][y]: # 이전 소비 비용이 더 작다면 무시
            continue
        else:
            for dx, dy in mv:
                nx, ny = x + dx, y + dy
                if any((nx < 0, nx >= n, ny < 0, ny >= n)): # 2차원 공간을 벗어나면 무시
                    continue

                next_cost = cost + costs[nx][ny]
                if next_cost < spend[nx][ny]:
                    spend[nx][ny] = next_cost
                    heapq.heappush(q, (next_cost, nx, ny))

    return spend[n - 1][n - 1]


t = int(input())
for i in range(t):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    print(dijkstra(n, costs))
    print(dijkstra_v2(n, costs))


''' TEST
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
''' # 20 19 36

# TEST
import unittest as ut

class TestSolution(ut.TestCase):
    def test_3_x_3(self):
        n = 3
        costs = [[5, 5, 4], \
                 [3, 9, 1], \
                 [3, 2, 7]]
        self.assertEqual(dijkstra(n, costs), 20)
        self.assertEqual(dijkstra_v2(n, costs), 20)

    def test_5_x_5(self):
        n = 5
        costs = [[3, 7, 2, 0, 1], \
                 [2, 8, 0, 9, 1], \
                 [1, 2, 1, 8, 1], \
                 [9, 8, 9, 2, 0], \
                 [3, 6, 5, 1, 5]]
        self.assertEqual(dijkstra(n, costs), 19)
        self.assertEqual(dijkstra_v2(n, costs), 19)

    def test_7_x_7(self):
        n = 7
        costs = [[9, 0, 5, 1, 1, 5, 3], \
                 [4, 1, 2, 1, 6, 5, 3], \
                 [0, 7, 6, 1, 6, 8, 5], \
                 [1, 1, 7, 8, 3, 2, 3], \
                 [9, 4, 0, 7, 6, 4, 1], \
                 [5, 8, 3, 2, 4, 8, 3], \
                 [7, 4, 8, 4, 8, 3, 4]]
        self.assertEqual(dijkstra(n, costs), 36)
        self.assertEqual(dijkstra_v2(n, costs), 36)

ut.main()