# N개의 집과 그 집들을 연결하는 M개의 길로 이루어진 마을을 2개로 분할할 때 길의
# 유지비 합의 최소값?
# (각 길에는 유지비가 존재하며, 모든 길은 양방향이다.)
# 조건 :
#   1. 분할된 각 마을에는 집이 1개이상 존재해야 한다.
#   2. 분할된 각 마을 안에는 집들이 서로 연결된 경로가 있어야 한다.
#   3. 분할된 마을 간의 길과 집들 간 필요없는 길은 모두 없앤다.

# 문제 풀이 전략
'''
    1. 전체 마을에 크루스칼 알고리즘을 수행해 각 길의 유지비 합을 최소로 만든다.
    2. 1번에서 구한 최소 신장 트리의 길 중 유지비가 가장 높은 길을 끊어 마을을 분리한다.
'''

def find_root(parent, node):
    if node != parent[node]:
        parent[node] = find_root(parent, parent[node])
    return parent[node]

def union_of_sets(parent, node1, node2):
    root1 = find_root(parent, node1)
    root2 = find_root(parent, node2)

    if root1 == root2: # 사이클이 발생하므로 True 반환
        return True
    elif root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1
    return False


# 집과 길의 개수 입력
n, m = map(int, input().split())

# 부모 테이블 각 집의 번호로 초기화
parent = [i for i in range(n + 1)]

roads = []

# 집 사이 연결된 길 정보 입력
for _ in range(m):
    h1, h2, cost = map(int, input().split())
    # 유지비 기준으로 정렬하기 위해 유지비를 첫 번째 원소로 한 tuple을 추가
    roads.append((cost, h1, h2))

# 크루스칼 알고리즘을 위한 오름차 정렬
roads.sort()

keeping_cost = 0
# 포함되는 길의 유지비 중 가장 큰 값
last_cost = 0

# 모든 길에 대해 크루스칼 알고리즘 수행
for cost, h1, h2 in roads:
    if not union_of_sets(parent, h1, h2):
        keeping_cost += cost
        last_cost = cost

print(keeping_cost - last_cost)


''' TEST
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
''' # 8



