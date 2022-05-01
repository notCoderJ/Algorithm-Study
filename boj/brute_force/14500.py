'''
  풀이
    n, m의 범위가 최대 500, 테트로미노 종류 5, 각 테트로미노를 90도씩 4번 회전 + 좌우 반전으로 동일하게 4번 회전 = 8
    (회전 시 동일한 모양도 중복 계산 시)
    총 500 * 500 * 5 * 8 = 10,000,000 연산으로 완전 탐색이 가능할 것이라 생각했다.
    하지만, 파이썬으로 시도했을 때 시간초과 판정을 받았다.
    결국, pypy로 제출하여 통과는 되었지만... 더 효율적인 다른 방법이 있을 것 같다😅
    (다시 풀어보고 민망한 현재 풀이를 갱신해야겠다;;)
    
    ver1. 모든 케이스 탐색
    1. 현위치를 기준으로 각 테트로미노의 종류별 위치 변화량을 정의한다.
    2. 주어진 종이의 좌표들을 순회하며 각 테트로미노에 대해
      0도, 90도, 180도, 270도 회전 시 테트로미노가 위치한 좌표를 구한다.
      (좌우 반전한 테트로미노에 대해서도 동일하게 반복)
    3. 2에서 구한 각 테트로미노의 위치가 종이 범위 내에 있으면
      max(현재 answer, 현재 테트로미노 위치에서 수의 합)를 구한다.
    
    ver2. dfs 풀이
    dfs를 사용한 다른 효율적인 풀이 방식을 참고하여 이해해보았다.
    해당 풀이는 아래 1, 2과정을 반복하면 된다.
    1. 주어진 종이의 각 좌표를 순회하며,
      해당 좌표에서 상하좌우 연결된 방문하지 않은 좌표에 대해 종이의 값을 누적하고 dfs를 수행한다.
    2. 현재 탐색한 좌표의 개수가 4개인 경우(0부터 시작하므로 3까지)
      지금까지 누적된 값과 현재 answer를 비교하여 최댓값을 answer에 저장한다.

    단, 여기서 주의할 점은 ㅏ, ㅗ, ㅜ, ㅓ와 같이 이어져 나갈 수 없는 형태가 존재하기 때문에
      탐색 좌표의 개수가 1일 때 다음 좌표로 이동하지 않고 다음 좌표의 종이 값만 누적한 후 현재 좌표에서 dfs를 재수행해야 한다는 것이다.
    
    추가로, 효율성을 높히기 위해 현재까지 탐색한 좌표에서
      "누적 값 + 종이 값 중 최댓값 * (3 - 현재까지 탐색 개수)" <= 현재 answer 값이라면
      탐색을 더 진행해도 무의미하므로 탐색을 종료시키면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

# ver1. 모든 케이스 탐색
def solution(m, n, paper):
  answer = 0
  tetromino = [
    ((0, 0), (0, 1), (0, 2), (0, 3)), # ㅡ
    ((0, 0), (0, 1), (1, 0), (1, 1)), # ㅁ
    ((0, 0), (1, 0), (2, 0), (2, 1)), # ㄴ
    ((0, 0), (1, 0), (1, 1), (2, 1)), # 번개
    ((0, 0), (0, 1), (0, 2), (1, 1)), # ㅜ
  ]

  def rotate90(pos):
    a, b, c, d = pos
    return [(-a[1], a[0]), (-b[1], b[0]), (-c[1], c[0]), (-d[1], d[0])]
  
  def reverse(pos):
    a, b, c, d = pos
    return [(a[0], -a[1]), (b[0], -b[1]), (c[0], -c[1]), (d[0], -d[1])]
  
  def calc_sum(i, j):
    nonlocal answer
    
    for t in tetromino:
      for p in [t, reverse(t)]:
        cur = p
        for _ in range(4):
          area_sum = 0
          for k in range(4):
            x, y = i + cur[k][0], j + cur[k][1]
            if 0 <= x < n and 0 <= y < m:
              area_sum += paper[x][y]
            else:
              break
          else:
            answer = max(answer, area_sum)
          cur = rotate90(cur)
      
  for i in range(n):
    for j in range(m):
      calc_sum(i, j)

  return answer

# ver2. dfs 풀이
def solution2(m, n, paper):
  answer = 0
  visited = [[False] * m for _ in range(n)]
  move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  max_val = max(map(max, paper))
  
  def dfs(x, y, cnt, total):
    nonlocal answer
    if answer >= total + max_val * (3 - cnt):
      return
    
    if cnt == 3:
      answer = max(answer, total)
      return
    
    for dx, dy in move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if cnt == 1:
          visited[nx][ny] = True
          dfs(x, y, cnt + 1, total + paper[nx][ny])
          visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx, ny, cnt + 1, total + paper[nx][ny])
        visited[nx][ny] = False
  
  for i in range(n):
    for j in range(m):
      visited[i][j] = True
      dfs(i, j, 0, paper[i][j])
      visited[i][j] = False
  
  return answer
  
if __name__ == '__main__':
  n, m = map(int, input().split())
  paper = [list(map(int, input().split())) for _ in range(n)]
  print(solution(m, n, paper))
  print(solution2(m, n, paper))