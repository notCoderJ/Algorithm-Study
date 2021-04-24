# 서로소 집합을 활용한 무방향 그래프 사이클 판별
# 1. 모든 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다.
# 2. 루트 노드가 서로 다르면 union연산을 실행하고 같으면 사이클이 발생한 것이다.

def find_root(node, parent):
    if node != parent[node]:
        parent[node] = find_root(parent[node], parent)
    return parent[node]

def union_of_sets(node1, node2, parent):
    root1 = find_root(node1, parent)
    root2 = find_root(node2, parent)
    if root1 == root2: # 사이클이 발생했으므로 True 반환
        return True
    elif root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1
    return False

# 노드 수와 간선(union 연산) 수 입력
v, e = map(int, input().split())

# 부모 테이블을 노드 자기 자신 값으로 초기화
parent = [i for i in range(v + 1)]

cycle = False

# 사이클 발생 확인
for _ in range(e):
    n1, n2 = map(int, input().split())
    if union_of_sets(n1, n2, parent):
        cycle = True
        break

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

''' TEST
3 3
1 2
1 3
2 3
''' # 사이클이 발생했습니다.