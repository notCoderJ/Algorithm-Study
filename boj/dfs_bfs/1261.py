'''
  풀이
    시작점에서 미로의 끝에 도달하려면 최소 몇개의 벽을 부숴야 하는지 구하는 문제이다.
    BFS 알고리즘을 사용하여 각 지점마다 상하좌우 방향을 탐색하고
    매 지점에서 벽을 부순 횟수를 최소로 하며 목적지까지 이동하면 되는데
    최단 거리를 구하는 것이 아니기 때문에
    같은 지점에서 벽을 부순 횟수가 더 적은 경우 중복 탐색이 가능한 것을 고려해야 한다.
    
    단순히 큐를 사용할 경우 어떤 지점에서 벽을 부순 횟수가
    최소가 되는 것을 보장하기 어렵다고 생각하여 우선순위 큐를 사용하였다.
    
    먼저, 각 지점의 벽을 부순 최소 횟수를 기록할 2차원 테이블을 무한대 값으로 초기화하고
    우선순위 큐에 시작점의 현재까지 벽을 부순 누적 횟수와 위치를 넣어준다.
    우선순위 큐로부터 벽을 부순 누적 횟수가 최소인 지점을 하나 꺼낸 후
    해당 지점에서 상하좌우 방향으로 이동할 때
    다음 지점의 벽을 부순 누적 횟수가 현재 기록 테이블 상 벽을 부순 횟수보다 적은 경우
    기록 테이블 값을 갱신하고 다음 지점의 벽을 부순 누적 횟수와 위치를 우선순위 큐에 넣고 위 과정을 반복한다.
    만약, 우선순위 큐에서 꺼낸 지점이 도착점이라면 현재까지 벽을 부순 누적 횟수를 출력하면 된다.
'''

import heapq
INF = int(1e9)

def solution():
  m, n = map(int, input().split())
  miro = [list(map(int, input())) for _ in range(n)]
  path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  record = [[INF] * m for _ in range(n)]
  record[0][0] = 0
  hq = [(0, 0, 0)]
  
  while hq:
    br, x, y = heapq.heappop(hq)
    if x == n - 1 and y == m - 1:
      print(br)
      return
    
    if record[x][y] < br:
      continue
    
    for dx, dy in path:
      nx, ny = x + dx, y + dy
      if 0 > nx or nx >= n or 0 > ny or ny >= m:
        continue
      
      nbr = br + miro[nx][ny]
      if nbr < record[nx][ny]:
        record[nx][ny] = nbr
        heapq.heappush(hq, (nbr, nx, ny))
  
if __name__ == '__main__':
  solution()