'''
  풀이
    처음 접근한 방법은 bfs나 dfs를 사용해서 섬의 외곽 좌표를 구한 다음
    각 좌표 간의 거리를 구하며 최단 거리를 얻으려고 했다.
    접근 방법은 틀리지 않았다고 생각하는데, 계속 틀렸다고 나와서 한참을 고생했다.
    틀린 이유를 알고보니 초기 최단 거리 값을 2 * n으로 설정해야하는데 n으로 설정했었다 -_-
    
    (이전 풀이)
    풀이한 방법은
    먼저, bfs를 사용해 주어진 지도에서 섬들을 탐색하며 섬들의 외곽 좌표들을 수집하였다.
    그 후 서로 다른 섬의 각 외곽 좌표 간의 거리를 구하면서 최단 거리를 계산하였다.
    여기서, 외곽 좌표 간의 거리는 "절댓값(x좌표 차이) + 절댓값(Y좌표 차이) - 1"로 계산할 수 있다.
    -1을 해주는 이유는 x, y 좌표차만 구해서 더하면 상대 외곽 좌표와 두 방향에서 만나게 되기 때문이다.
    
    (신규 풀이)
    bfs를 이용해서 주어진 지도의 각 섬들을 서로 다른 번호로 라벨링하며 섬의 외곽 좌표를 수집한다.
    수집한 각 외곽 좌표에 대해 bfs를 수행하며 다른 섬까지의 최단 거리를 구하고, 이 중에 가장 짧은 최단 거리를 선택하면 된다.
    
    이전 풀이의 경우 모든 좌표 간의 차를 구하는 과정에서 많은 시간이 소요되었는지 약 6000ms의 수행시간이 나왔다.
    좀 더 효율적으로 변경하기 위해 각 외곽 좌표에서 bfs를 사용해 최단 거리를 구하는 방법으로 변경한 결과 약 300ms로
    수행 시간이 20배나 감소되었다.
'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
  n = int(input())
  Map = [input().split() for _ in range(n)]
  label = 1
  answer = 2 * n
  edges = set()

  check_out = lambda x, y: False if 0 <= x < n and 0 <= y < n else True

  def labeling(a, b):
    q = deque([(a, b)])
    island = set()

    while q:
      x, y = q.popleft()
      for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if check_out(nx, ny):
          continue
        if Map[nx][ny] == '1':
          Map[nx][ny] = label
          q.append((nx, ny))
        if Map[nx][ny] == '0':
          island.add((x, y))
    return island
  
  def find_shortest(a, b):
    nonlocal answer
    q = deque([(a, b, 0)])
    visited = [[False] * n for _ in range(n)]
    while q:
      x, y, d = q.popleft()
      for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if check_out(nx, ny) or visited[nx][ny]:
          continue
        if Map[nx][ny] == '0':
          visited[nx][ny] = True
          q.append((nx, ny, d + 1))
        elif Map[nx][ny] != Map[i][j]:
          answer = min(answer, d)
          return
  
  # labeling
  for i in range(n):
    for j in range(n):
      if Map[i][j] == '1':
        Map[i][j] = label
        edges |= labeling(i, j)
        label += 1
        
  # find shortest distance
  for i, j in edges:
    find_shortest(i, j)
  
  print(answer)
  
if __name__ == '__main__':
  solution()
  

# 이전 풀이  
# def solution():
#   n = int(input())
#   Map = [input().split() for _ in range(n)]
#   end_point = []
  
#   def bfs(a, b):
#     q = deque([(a, b)])
#     island = set()

#     while q:
#       x, y = q.popleft()
#       outline = False
#       for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         if 0 > nx or nx >= n or 0 > ny or ny >= n:
#           continue
#         if Map[nx][ny] == '1':
#           Map[nx][ny] = '#'
#           q.append((nx, ny))
#         if Map[nx][ny] == '0':
#           outline = True
#       if outline:
#         island.add((x, y))

#     return island
    
#   for i in range(n):
#     for j in range(n):
#       if Map[i][j] == '1':
#         end_point.append(bfs(i, j))

#   answer = 2 * n
#   for i in range(len(end_point) - 1):
#     for j in range(i + 1, len(end_point)):
#       for x1, y1 in end_point[i]:
#         for x2, y2 in end_point[j]:
#           answer = min(answer, abs(x1 - x2) + abs(y1 - y2) - 1)
#   print(answer)