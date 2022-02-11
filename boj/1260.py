'''
  풀이
    DFS와 BFS 알고리즘을 연습해볼 수 있는 간단한 문제였다.
    문제에서 요구하는대로 DFS 알고리즘과 BFS 알고리즘을 구현한 후
    주어진 시작 정점 번호에서 DFS와 BFS를 각각 수행한 후 출력하였다.
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1, n + 1):
  graph[i].sort()


def dfs(node, visited):
  visited[node] = True
  print(node, end=' ')

  for i in graph[node]:
    if not visited[i]:
      dfs(i, visited)

def bfs():
  visited = [False] * (n + 1)
  visited[v] = True
  dq = deque([v])
  
  while dq:
    node = dq.popleft()
    print(node, end=' ')

    for i in graph[node]:
      if not visited[i]:
        visited[i] = True
        dq.append(i) 

def solution():
  dfs(v, [False] * (n + 1))
  print()
  bfs()
  
if __name__ == '__main__':
  solution()