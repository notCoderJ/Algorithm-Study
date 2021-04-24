# 0 ~ N번까지의 번호가 부여된 학생들에게 다음 두 연산을 사용할 때
# M개의 연산을 수행한 후 '같은 팀 여부 확인'연산에 대한 연산 결과?
# (처음에는 모든 학생이 서로 다른 팀이므로 총 N + 1개의 팀이 존재)
# 2가지 연산 :
#   1. '팀 합치기' : 두 팀을 합친다.
#   2. '같은 팀 여부 확인' : 특정한 두 학생이 같은 팀에 속하는 지 확인한다.

def find_root(parent, node):
    if node != parent[node]:
        parent[node] = find_root(parent, parent[node])
    return parent[node]

def union_of_sets(parent, node1, node2):
    root1 = find_root(parent, node1)
    root2 = find_root(parent, node2)

    if root1 >= root2:
        parent[root1] = root2
    else:
        parent[root2] = root1

# 팀 마지막 번호와 연산 수 입력
n, m = map(int, input().split())

# 부모 테이블 각 팀의 자기자신 값으로 초기화
parent = [i for i in range(n + 1)]

for _ in range(m):
    oper, n1, n2 = map(int, input().split())
    if oper == 0:
        union_of_sets(parent, n1, n2)
    elif find_root(parent, n1) == find_root(parent, n2):
        print("YES")
    else:
        print("NO")


''' TEST
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
''' # NO NO YES