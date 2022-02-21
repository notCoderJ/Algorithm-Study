'''
  풀이
    네트워크 상의 컴퓨터들을 노드로, 컴퓨터 간에 감염 시간을 거리로 생각하면
    그래프의 어떤 한 노드에서 다른 노드까지의 최단 거리를 구하는 것과 동일하므로 다익스트라 알고리즘을 사용하였다.
    단, 특정 컴퓨터가 감염되는 최소 시간을 구하는 것이 아니고, 모든 컴퓨터가 감영되는 최소 시간을 구하는 것이므로
    각 컴퓨터가 감영되는 최소 시간 중 가장 오래 걸리는 시간을 출력해야 한다.

    먼저, 각 컴퓨터가 감염되는 최소 시간을 기록할 테이블을 무한대 값으로 초기화한 후
    감염된 컴퓨터를 시작으로 연결된 각 컴퓨터마다 이전 기록된 감염 시간 > 현재 감염 예상 시간인 경우
    해당 컴퓨터의 감영까지 걸리는 시간과 컴퓨터 번호를 우선순위 큐에 넣고
    감염 시간이 빠른 순으로 하나씩 꺼내며, 기록 테이블을 갱신하였다.
    감염된 컴퓨터 수와 모든 컴퓨터가 감염되는 최소 시간을 구하기 위해
    테이블 갱신 과정에서 현재 꺼낸 컴퓨터가 최소 감염 시간이 될 때마다
    감염된 컴퓨터 수와 모든 컴퓨터가 감염되는 시간을 갱신해주었다.
'''

import sys
import heapq

INF = int(1e9)
input = lambda: sys.stdin.readline().strip()

def solution():
  n, d, c = map(int, input().split())
  network = [[] for _ in range(n + 1)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    network[b].append((a, s))
  
  cnt, time = 0, -1
  visited = [INF] * (n + 1)
  visited[c] = 0
  hq = [(0, c)]
  while hq:
    ctime, cur = heapq.heappop(hq)
    if visited[cur] < ctime:
      continue

    time = max(time, ctime)
    cnt += 1
    
    for cp, t in network[cur]:
      ntime = ctime + t
      if visited[cp] > ntime:
        visited[cp] = ntime
        heapq.heappush(hq, (ntime, cp))

  print(cnt, time)
        
if __name__ == '__main__':
  for _ in range(int(input())):
    solution()