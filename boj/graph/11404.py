'''
  풀이
    문제 이름 그대로 플로이드 와샬 알고리즘을 사용하면 바로 풀 수 있는 문제였다.
    단순히, 알고리즘을 알고 있는지 확인하는 문제였기 때문에 고려해줄만한 사항이 없었다.
    그래도 하나만 꼽아보자면 처음 노선에 대한 그래프를 생성할 때
    동일 경로에 대해 비용이 다른 노선이 존재할 수 있기 때문에
    이점을 주의하여 해당 경로에서 최소 비용을 저장해주어야 한다는 점이다.
'''

import sys
input = lambda: sys.stdin.readline().strip()
INF = int(1e9)

def solution():
  n = int(input())
  m = int(input())
  graph = [[INF] * (n + 1) for _ in range(n + 1)]
  for i in range(1, n + 1):
    graph[i][i] = 0
    
  for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
  
  def floyd():
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        for k in range(1, n + 1):
          graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
  
  floyd()
  
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
  
if __name__ == '__main__':
  solution()
