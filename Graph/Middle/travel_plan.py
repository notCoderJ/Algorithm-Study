# N개의 여행지를 연결하는 도로 정보가 주어질 때 한울이의 여행 계획이 가능한지 판별하라.
# (연결된 도로는 양방향 이동이 가능하다.)

# 문제 풀이 전략
'''
    해당 문제는 여행 계획 내 포함되는 모든 여행지들이 같은 집합인지 확인하여 해결할 수 있다.
    여행지 간 연결된 도로가 양방향이므로 '무방향 그래프'에 해당하고 주어진 도로 정보를
    이용해 서로소 집합을 구성하면 여행 계획이 가능한지 확인할 수 있다.
'''

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find_root(node):
    if node != parent[node]:
        parent[node] = find_root(parent[node])
    return parent[node]

def union_of_sets(n1, n2):
    root1 = find_root(n1)
    root2 = find_root(n2)

    if root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1


for i in range(n):
    connected = list(map(int, input().split()))
    for j in range(n):
        if connected[j] == 1: # 여행지 간 도로가 연결되어 있으면 서로소 집합에 포함시킨다
            union_of_sets(i + 1, j + 1)

plans = list(map(int, input().split()))

valid = True
for i in range(m - 1):
    # 여행 계획 내 같은 집합이 아닌 여행지가 하나라도 존재할 경우 불가능으로 판정한다
    if find_root(plans[i]) != find_root(plans[i + 1]):
        valid = False

if valid:
    print("YES")
else:
    print("NO")


''' TEST
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0 
1 0 0 0 0
2 3 4 3
''' # YES