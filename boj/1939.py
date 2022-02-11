'''
  풀이
    먼저, 공장 간 이동 경로를 탐색하기 위해 DFS나 BFS를 사용해야겠다고 생각했다.
    하지만, 서로 같은 두 섬 간에 중량이 다른 복수의 다리가 주어질 수 있기 때문에
    단순히 DFS나 BFS로 경우를 나누어 탐색하기는 어렵다는 생각이 들었다.
    그래서, 공장 간 이동 시 최대 중량을 이분 탐색의 대상으로 잡고 Parametric Search를 적용하며
    각 중간 값에 대해 DFS 또는 BFS를 사용해 해당 중량이 허용되는지 확인하였다.
    
    여기서, 한가지 문제가 있었는데, 처음에는 DFS를 사용해 판별을 시도하였고 메모리 초과 판정을 받았다.
    메모리 제한이 128MB로 작았기 때문에 DFS의 재귀 호출을 수행하며 메모리 초과가 될 수 있다는 생각이 들었다.
    이를 반복문 형식으로 변경하면 DFS로도 가능할 듯 싶었지만, BFS로 방법을 변경하여 해당 문제를 해결했다.
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
  f1, f2 = map(int, input().split())

  def bfs(target):
    visited = [False] * (n + 1)
    visited[f1] = True
    dq = deque([f1])
    while dq:
      node = dq.popleft()
      if node == f2:
        return True
      for f, w in graph[node]:
        if w >= target and not visited[f]:
          visited[f] = True
          dq.append(f)
    return False

  left, right = 1, int(1e9)
  while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
      answer = mid
      left = mid + 1
    else:
      right = mid - 1
  
  print(answer)

if __name__ =='__main__':
  solution()