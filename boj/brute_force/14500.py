'''
  풀이
    n, m의 범위가 최대 500, 테트로미노 종류 5, 각 테트로미노를 90도씩 4번 회전 + 좌우 반전으로 동일하게 4번 회전 = 8
    (회전 시 동일한 모양도 중복 계산 시)
    총 500 * 500 * 5 * 8 = 10,000,000 연산으로 완전 탐색이 가능할 것이라 생각했다.
    하지만, 파이썬으로 시도했을 때 시간초과 판정을 받았다.
    결국, pypy로 제출하여 통과는 되었지만... 더 효율적인 다른 방법이 있을 것 같다😅
    (다시 풀어보고 민망한 현재 풀이를 갱신해야겠다;;)
    
    1. 현위치를 기준으로 각 테트로미노의 종류별 위치 변화량을 정의한다.
    2. 주어진 종이의 좌표들을 순회하며 각 테트로미노에 대해
      0도, 90도, 180도, 270도 회전 시 테트로미노가 위치한 좌표를 구한다.
      (좌우 반전한 테트로미노에 대해서도 동일하게 반복)
    3. 2에서 구한 각 테트로미노의 위치가 종이 범위 내에 있으면
      max(현재 answer, 현재 테트로미노 위치에서 수의 합)를 구한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

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
  
if __name__ == '__main__':
  n, m = map(int, input().split())
  paper = [list(map(int, input().split())) for _ in range(n)]
  print(solution(m, n, paper))