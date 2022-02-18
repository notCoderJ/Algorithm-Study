'''
  풀이
    한 지점에서 다른 지점까지의 최단 거리를 구하는 일반적인 다익스트라 알고리즘에서 살짝 변형한 유형같다.
    해당 문제는 지점 간 최단 거리를 구하는 것이 아닌 도착 경로의 가중치 중 최댓값이 최소가 되도록 하는 문제이다.
    
    그러므로 고려해야할 대상은 각 교차로까지 도착하는데 구간 최대 통행료이고,
    다익스트라 알고리즘을 적용할 때 우선순위 큐를 사용해서 순차적으로 꺼내야하는 대상은
    각 교차로까지의 최단 거리가 아닌 "해당 교차로까지 경로 중 구간 최대 통행료"이다.
    
    따라서, 우선순위 큐를 사용해서 최대 통행료가 가장 적은 교차로를 구하고 연결된 다음 교차로까지 가는 비용을 계산하여
    예산 안에 있으면 (다음 교차로까지 최대 통행료, 다음 교차로까지 누적 비용, 다음 교차로 번호)를 다시 우선순위 큐에 추가하고 위 과정을 반복하면 된다.
    만약, 우선순위 큐에서 꺼낸 교차로가 목적지라면 현재 최대 통행료를 출력하면 된다.
    (우선순위 큐를 사용했기 때문에 해당 목적지까지 최대 통행료가 낮은 순으로 꺼내진다.)
    
    여기서, 주의할 점은 두 지점 간 이동 방향에 대해 방문처리를 해주어야 한다.
    방문처리를 하지 않는 경우 같은 이동 방향에 대해 중복 처리될 수 있어 시간 초과가 발생한다.
    아래 풀이에서는 각 교차로 간 2차원 배열을 만들어 동일 이동 방향에 대해 방문처리를 해주었다.
'''

import heapq
INF = int(1e9)

def solution():
  n, m, a, b, c = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
    
  visited = [[False] * (n + 1) for _ in range(n + 1)]
  hq = [(0, 0, a)]
  while hq:
    fee, total, cur = heapq.heappop(hq)
    if cur == b:
      print(fee)
      return
    
    for t, w in graph[cur]:
      next = total + w
      if next <= c and not visited[cur][t]:
        visited[cur][t] = True
        heapq.heappush(hq, (max(fee, w), next, t))

  print(-1)
  
if __name__ == '__main__':
  solution()