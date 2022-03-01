'''
  풀이
    처음 접근한 방법은 bfs나 dfs를 사용해서 섬의 외곽 좌표를 구한 다음
    각 좌표 간의 거리를 구하며 최단 거리를 얻으려고 했다.
    접근 방법은 틀리지 않았다고 생각하는데, 계속 틀렸다고 나와서 한참을 고생했다.
    틀린 이유를 알고보니 초기 최단 거리 값을 2 * n으로 설정해야하는데 n으로 설정했었다 -_-
    
    풀이한 방법은
    먼저, bfs를 사용해 주어진 지도에서 섬들을 탐색하며 섬들의 외곽 좌표들을 수집하였다.
    그 후 서로 다른 섬의 각 외곽 좌표 간의 거리를 구하면서 최단 거리를 계산하였다.
    여기서, 외곽 좌표 간의 거리는 "절댓값(x좌표 차이) + 절댓값(Y좌표 차이) - 1"로 계산할 수 있다.
    -1을 해주는 이유는 x, y 좌표차만 구해서 더하면 상대 외곽 좌표와 두 방향에서 만나게 되기 때문이다.
'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  Map = [input().split() for _ in range(n)]
  end_point = []
  
  def bfs(a, b):
    q = deque([(a, b)])
    island = set()

    while q:
      x, y = q.popleft()
      outline = False
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
          continue
        if Map[nx][ny] == '1':
          Map[nx][ny] = '#'
          q.append((nx, ny))
        if Map[nx][ny] == '0':
          outline = True
      if outline:
        island.add((x, y))

    return island
    
  for i in range(n):
    for j in range(n):
      if Map[i][j] == '1':
        end_point.append(bfs(i, j))

  answer = 2 * n
  for i in range(len(end_point) - 1):
    for j in range(i + 1, len(end_point)):
      for x1, y1 in end_point[i]:
        for x2, y2 in end_point[j]:
          answer = min(answer, abs(x1 - x2) + abs(y1 - y2) - 1)
  print(answer)
  
if __name__ == '__main__':
  solution()