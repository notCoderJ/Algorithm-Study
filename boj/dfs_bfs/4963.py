'''
  풀이
    dfs나 bfs를 사용하면 간단하게 풀 수 있는 문제였다.
    
    주어진 테스트 케이스의 각 좌표를 순회하며,
    해당 좌표가 땅이고 방문한 적이 없으면 섬의 수(answer)를 1 늘리고 dfs(or bfs)를 수행한다.
    dfs를 수행할 때는 현재 위치에서 상하좌우, 대각선에 땅이 존재하는지 확인하고
    땅인 경우 dfs를 반복 수행하며 방문 처리를 해준다.
    모든 좌표 순회가 완료되면 현재 섬의 수(answer)를 출력한다.
'''

import sys
sys.setrecursionlimit(int(1e8))
input = lambda: sys.stdin.readline().strip()

def solution(w, h, _map):
  answer = 0
  move = [(1, 0), (0, 1), (-1, 0), (0, -1), \
          (1, 1), (-1, -1), (1, -1), (-1, 1)]
  visited = [[False] * w for _ in range(h)]
  
  def dfs(x, y):
    visited[x][y] = True

    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < h and 0 <= ny < w \
        and not visited[nx][ny] and _map[nx][ny] != '0':
        dfs(nx, ny)
  
  for i in range(h):
    for j in range(w):
      if _map[i][j] != '0' and not visited[i][j]:
        answer += 1
        dfs(i, j)
  
  return answer
  
if __name__ == '__main__':
  while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
      break
    
    _map = [input().split() for _ in range(h)]
    print(solution(w, h, _map))
