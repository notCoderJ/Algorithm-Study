# 한 도시에서 출발해 다른 도시로 가는 m개의 버스가 있는 n개의 도시에서
# 모든 도시 쌍 (A, B)에 대한 도시 A에서 B로 가는 최소 비용은?


INF = int(1e9)

# 플로이드 워셜 수행
def floyd_warshall(cost):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])


n = int(input())
m = int(input())

cost = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c) # a도시와 b도시를 연결하는 노선이 여럿일 수 있다

floyd_warshall(cost)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        itoj = cost[i][j]
        if itoj == INF:
            print(0, end=' ')
        else:
            print(itoj, end=' ')
    print()


''' TEST
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
''' # 0 2 3 1 4
    # 12 0 15 2 5
    # 8 5 0 1 1
    # 10 7 13 0 3
    # 7 4 10 6 0
