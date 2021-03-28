# 그래프를 인접 행렬로 표현하는 예제

INF=999999999 # 무한 값 지정

# 해당 노드에서 모든 노드에 대한 가중치 정보를 저장한다.
graph_matrix = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

for row in graph_matrix:
    print(row)
