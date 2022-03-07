'''
  풀이
    단순히 dfs와 bfs의 개념을 알아보는 쉬운 문제이다.
    주어진 정보를 이용해 그래프를 만든 후
    모든 노드에 대해 방문하지 않은 노드가 있으면
    dfs나 bfs를 이용해 탐색하며, 이어진 노드들을 방문처리하면 된다.
    이때, 방문하지 않은 노드가 있다는 것은 다른 하나의 연결 요소가 있다는 것이므로
      노드 탐색 전에 요소의 개수를 하나 증가시키면 된다.
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = 0
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  visited = [False] * (n + 1)
  
  def bfs(node):
    q = deque([node])
    visited[node] = True
    
    while q:
      cur = q.popleft()
      for i in graph[cur]:
        if not visited[i]:
          visited[i] = True
          q.append(i)
  
  for i in range(1, n + 1):
    if not visited[i]:
      answer += 1
      bfs(i)
  
  print(answer)
  
if __name__ == '__main__':
  solution()