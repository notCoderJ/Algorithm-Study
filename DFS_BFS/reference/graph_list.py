# 그래프를 인접 리스트로 표현하는 예제

# 해당 노드에 연결된 노드와 가중치 정보를 저장한다.
graph_list = [[] for _ in range(3)] # 인접 리스트를 표현할 2차원 리스트 초기화

# 노드 0에 연결된 노드와 가중치를 저장
graph_list[0].append((1, 7))
graph_list[0].append((2, 5))

# 노드 1에 연결된 노드와 가중치를 저장
graph_list[1].append((0, 7))

# 노드 2에 연결된 노드와 가중치를 저장
graph_list[2].append((0, 5))

for row in graph_list:
    print(row)