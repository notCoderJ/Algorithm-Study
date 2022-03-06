'''
  풀이
    다익스트라 풀이
      1. 주어진 도로 정보로 그래프를 만들 때 변경횟수를 함께 포함시켜 만들어준다.
      예를 들어, 1 -> 2, 3 <-> 4 와 같이 단방향, 양방향이 주어지면
        graph[출발지점] = [(도착지점, 변경횟수), ...]
        graph[1] = [(2, 0)], graph[3] = [(4, 0)], graph[4] = [(3, 0)]
        graph[2] = [(1, 1)] (단방향으로 주어진 경우 변경횟수를 1로 하여 반대방향에 대해 추가해준다.)
      2. 1에서 구한 그래프를 이용해 가능한 모든 지점마다 다익스트라 알고리즘을 적용하며 다른 지점들로 가는 최소 변경횟수를 구한다.
        이때, 다익스트라 알고리즘에서 비교 대상은 각 지점 간 이동하기 위한 변경 횟수이다.
      3. 주어지는 테스트 케이스마다 2에서 구한 최소 변경횟수에 기반하여 최소 변경횟수를 출력한다.
    
    플로이드 와샬 풀이
      1. 주어진 도로 정보를 이용해 인접행렬 형태로 모든 지점 간 이동 시 변경횟수에 대한 그래프를 만들어준다.
        이때, 변경횟수를 초기화하는 방법은 다익스트라 풀이와 동일하다.
      2. 1에서 구한 그래프에 플로이드 와샬 알고리즘을 적용하여 모든 지점 간 이동 시 최소 변경횟수를 구한다.
      3. 주어지는 테스트 케이스마다 2에서 구한 테이블에 기반하여 각각 최소 변경횟수를 출력한다.
'''

import sys
import heapq
input = lambda: sys.stdin.readline().strip()
INF = int(1e9)

# 다익스트라 풀이
def solution(start, graph):
  visited = [INF] * (n + 1)
  visited[start] = 0
  hq = [(0, start)]
  
  while hq:
    cur_cnt, cur = heapq.heappop(hq)
    
    for next, cnt in graph[cur]:
      next_cnt = cur_cnt + cnt
      if visited[next] > next_cnt:
        visited[next] = next_cnt
        heapq.heappush(hq, (next_cnt, next))

  return visited
  
if __name__ == '__main__':
  n, m = map(int, input().split())
  graph = [[] * (n + 1) for _ in range(n + 1)]
    
  for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u].append((v, 0))
    graph[v].append((u, [1, 0][b == 1]))

  bidirect = [[]]
  for i in range(1, n + 1):
    bidirect.append(solution(i, graph))
  
  for _ in range(int(input())):
    s, e = map(int, input().split())
    print(bidirect[s][e])


# 플로이드 와샬 풀이
# def solution(n, graph):
#   for i in range(1, n + 1):
#     for j in range(1, n + 1):
#       for k in range(1, n + 1):
#         graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
  
# if __name__ == '__main__':
#   n, m = map(int, input().split())
#   graph = [[INF] * (n + 1) for _ in range(n + 1)]
#   for i in range(n + 1):
#     graph[i][i] = 0
    
#   for _ in range(m):
#     u, v, b = map(int, input().split())
#     graph[u][v] = 0
#     graph[v][u] = 0 if b == 1 else 1
  
#   solution(n, graph)
      
#   for _ in range(int(input())):
#     s, e = map(int, input().split())
#     print(graph[s][e])