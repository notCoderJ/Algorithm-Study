# 크루스칼(kruskal) 알고리즘 : 최소 신장 트리를 찾는 알고리즘

# 루트 노드 탐색
def find_root(parent, node):
    if node != parent[node]:
        parent[node] = find_root(parent, parent[node])
    return parent[node]

# 사이클 발생을 확인하고 union연산을 수행
def union_of_sets(parent, node1, node2):
    root1 = find_root(parent, node1)
    root2 = find_root(parent, node2)
    if root1 == root2: # 사이클 발생
        return True
    elif root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1
    return False


# 노드와 간선 수를 각각 입력
v, e = map(int, input().split())

# 부모 테이블 노드 자기자신 값으로 초기화
parent = [i for i in range(v + 1)]

# 간선 정보 입력
edges = [list(map(int, input().split())) for _ in range(e)]

# 간선의 비용에 따라 간선을 오름차 정렬
edges.sort(key=lambda x:x[2])

# 최소 신장 트리를 위한 비용
min_cost = 0

# 간선을 하나씩 확인하며 사이클 발생 확인
for a, b, c in edges:
    # 사이클이 발생하지 않으면 최소 신장 트리에 포함
    if not union_of_sets(parent, a, b):
        min_cost += c

print(min_cost)

''' TEST
7 9
1 2 29
1 5 75
2 3 35 
2 6 34 
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
''' # 159