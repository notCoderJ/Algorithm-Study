'''
  풀이
    해당 문제는 각 위치마다 x - 1, x + 1, 2 * x 지점의 정점들이 연결된 그래프로 해석하여 풀 수 있다.
    따라서, BFS와 Dijkstra 알고리즘을 이용하여 풀이하였다.
    
    1. BFS 풀이
      각 지점 x에서 0 이상 10만 이하의 범위 내에 있는 방문하지 않은 2 * x, x - 1, x + 1 지점들과 누적 시간을
      큐에 넣고, 방문처리한 후 큐에서 하나씩 꺼내 위 과정을 반복하며 x가 k가 될 때 누적 시간을 출력하면 된다.
      (이때, 주의할 점은 큐에 각 지점을 넣을 때 반드시 "x + 1을 가장 나중에" 넣어야 한다는 것이다.)
      
      예를 들어 0에서 2로 가는 최단 시간을 구할 때 x - 1, x + 1, 2 * x 순으로 큐에 넣는다고 가정해보자.
      (a, b)에서 a를 지점 번호, b를 누적 시간이라 하면
        처음 0 -> (1, 1) 큐에 추가, -1, 0은 범위 이탈과 이미 방문으로 제외
        1 -> (2, 2) 큐에 추가, 여기서 문제가 발생한다. x + 1도 2가 되고 2 * x도 2가 된다.
        2 -> 누적 시간 2 출력, x + 1을 먼저 처리했기 때문에 누적 시간이 최소가 아니게 된다.
        
    2. Dijkstra 풀이
      BFS 풀이는 큐에 넣는 순서를 고려해야하는 문제를 가지고 있는데,
      Dijkstra 알고리즘을 사용하면 이 문제를 해결할 수 있다.
      
      각 위치마다 최단 시간을 기록할 테이블을 무한대 값으로 초기화한 후
      우선순위 큐에서 누적 시간이 가장 짧은 지점을 하나 꺼내
      다음 이동 지점들의 누적 시간을 구하고 각각 현재 테이블 값과 비교한다.
      다음 지점의 누적 시간 < 현재 테이블의 누적 시간이면
      해당 위치의 테이블 값을 다음 지점의 누적 시간으로 갱신하고
      우선순위 큐에 누적 시간과 다음 이동 위치를 넣어준다.
      우선순위 큐에서 꺼낸 위치가 k가 될 때까지 위 과정을 반복하며 k지점의 최단 시간을 구하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
MAX = 100001

# 1. BFS
from collections import deque

def solution():
  visited = [False] * MAX
  visited[n] = True
  dq = deque([(n, 0)])
  
  while dq:
    l, t = dq.popleft()
    if l == k:
      print(t)
      return
    for nl, nt in [(2 * l, t), (l - 1, t + 1), (l + 1, t + 1)]:
      if 0 <= nl < MAX and not visited[nl]:
        visited[nl] = True
        dq.append((nl, nt))
  
# 2. Dijkstra
import heapq

def solution2():
  visited = [MAX] * MAX
  hq = [(0, n)]
  
  while hq:
    ct, cx = heapq.heappop(hq)
    if cx == k:
      print(ct)
      return
    
    if visited[cx] < ct:
      continue
    
    for nx, nt in [(cx - 1, ct + 1), (cx + 1, ct + 1), (2 * cx, ct)]:
      if 0 <= nx < MAX and visited[nx] > nt:
        visited[nx] = nt
        heapq.heappush(hq, (nt, nx))
  
if __name__ == '__main__':
  solution()
  solution2()