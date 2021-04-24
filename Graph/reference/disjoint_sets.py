# 서로소 집합 알고리즘

# 1. 특정 노드가 속한 루트 노드(집합)를 찾는 일반적인 find 함수
def find_root(node, parent):
    if node != parent[node]:
        return find_root(parent[node], parent)
    return node

# 2. 경로 압축(Path Compression)을 이용해 개선한 find 함수
def find_root_fast(node, parent):
    if node != parent[node]:
        parent[node] = find_root_fast(parent[node], parent)
    return parent[node]

# 두 노드가 속한 집합을 합치는 Union 연산
def union_of_sets(node1, node2, parent):
    # root1 = find_root(node1, parent)
    # root2 = find_root(node2, parent)
    root1 = find_root_fast(node1, parent)
    root2 = find_root_fast(node2, parent)
    if root1 >= root2:
        parent[root1] = root2
    else:
        parent[root2] = root1

# 노드 수와 간선(union 연산) 수 입력
v, e = map(int, input().split())

# 부모 테이블을 노드 자기 자신 값으로 초기화
parent = [i for i in range(v + 1)]

# union 연산을 입력받고 연산 수행
for _ in range(e):
    n1, n2 = map(int, input().split())
    union_of_sets(n1, n2, parent)

# 각 노드가 속한 집합과 부모 테이블 출력
print("노드가 속한 집합 : ", end='')
for i in range(1, v + 1):
    # print(find_root(i, parent), end=' ')
    print(find_root_fast(i, parent), end=' ')

print()

print("부모 테이블 : ", end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

''' TEST
6 4
1 4
2 3
2 4
5 6
''' # 노드가 속한 집합 : 1 1 1 1 5 5 / 부모 테이블 : 1 1 2 1 5 5
    # 경로 압축 시 -> 노드가 속한 집합 : 1 1 1 1 5 5 / 부모 테이블 : 1 1 1 1 5 5