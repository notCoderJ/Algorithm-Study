'''
  풀이
    해당 문제는 각 위치마다 x - 1, x + 1, 2 * x 지점의 정점들이 연결된 그래프로 해석하여 풀 수 있다.
    
    BFS를 이용한 풀이
      각 지점 x에서 0 이상 10만 이하의 범위 내에 있는 방문하지 않은 2 * x, x - 1, x + 1 지점들과 누적 시간을
      큐에 넣고, 방문처리한 후 큐에서 하나씩 꺼내 위 과정을 반복하며 x가 k가 될 때 누적 시간을 출력하면 된다.
      (이때, 주의할 점은 큐에 각 지점을 넣을 때 반드시 "x + 1을 가장 나중에" 넣어야 한다는 것이다.)
      
      예를 들어 0에서 2로 가는 최단 시간을 구할 때 x - 1, x + 1, 2 * x 순으로 큐에 넣는다고 가정해보자.
      (a, b)에서 a를 지점 번호, b를 누적 시간이라 하면
        처음 0 -> (1, 1) 큐에 추가, -1, 0은 범위 이탈과 이미 방문으로 제외
        1 -> (2, 2) 큐에 추가, 여기서 문제가 발생한다. x + 1도 2가 되고 2 * x도 2가 된다.
        2 -> 누적 시간 2 출력, x + 1을 먼저 처리했기 때문에 누적 시간이 최소가 아니게 된다.
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())

# 1. BFS
def solution():
  visited = [False] * 100001
  visited[n] = True
  dq = deque([(n, 0)])
  
  while dq:
    l, t = dq.popleft()
    if l == k:
      print(t)
      return
    for nl, nt in [(2 * l, t), (l - 1, t + 1), (l + 1, t + 1)]:
      if 0 <= nl <= 100000 and not visited[nl]:
        visited[nl] = True
        dq.append((nl, nt))
  
# 2. Dijkstra
def solution2():
  print()
  
if __name__ == '__main__':
  solution()
  solution2()