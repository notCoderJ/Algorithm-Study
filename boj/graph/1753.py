'''
  풀이
    주어진 시작 정점부터 각 정점까지의 최단경로를 묻는 문제이므로
    기본적인 다익스트라 알고리즘을 사용하여 풀이하였다.
    
    먼저, 주어진 경로들로 그래프를 생성한 후 각 정점까지의 거리를 기록할 테이블을 무한대 값으로 초기화하였다.
    그 다음, 시작 정점부터 이동 거리가 가장 짧은 정점을 하나씩 탐색하며 테이블에 각 정점까지의 최단 거리를 갱신해주었다.
    이때, 우선순위 큐에 해당 정점까지의 거리와 정점 번호를 추가하며 매번 가장 짧게 이동하는 정점을 구하였다.
    테이블이 완성된 후에는 각 정점의 갱신된 최단 거리를 출력하였고 여전히 무한대 값인 경우 'INF'를 출력해주었다.
'''

import sys
import heapq
input = lambda: sys.stdin.readline().strip()
INF = int(1e9)

def solution():
  V, E = map(int, input().split())
  start = int(input())
  graph = [[] for _ in range(V + 1)]
  for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
  
  dist = [INF] * (V + 1)
  dist[start] = 0
  hq = [(0, start)]
  
  while hq:
    cur_dist, cur = heapq.heappop(hq)
    if cur_dist > dist[cur]:
      continue
    
    for n, d in graph[cur]:
      next = cur_dist + d
      if next < dist[n]:
        dist[n] = next
        heapq.heappush(hq, (next, n))

  print(*[[n, 'INF'][n == INF] for n in dist[1:]], sep='\n')
  
if __name__ == '__main__':
  solution()