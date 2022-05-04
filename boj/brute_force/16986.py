'''
  풀이
    풀이가...;; 시간 초과는 면했지만 참...😅(다른 방법으로 다시 풀어봐야겠다🔥)
    처음에는 경기 진행 상대를 선택하고 승패 케이스로 나누어 dfs를 수행하는 방식으로 풀었는데,
    기저 조건 설정 오류로 33%에서 실패가 되었다...
    
    그래서, 문제의 예시 설명 중 `지우가 가능한 모든 손동작을 한 번씩 다 낸 후` 이 말에 힌트를 얻어 다음과 같이 풀었다.
    1. 지우가 낼 수 있는 가능한 손동작을 한 번씩 포함한 모든 경우의 수를 구한다.(순서 고려)
    2. 1번에서 구한 각 경우에 대해 최대 3 * (k - 1) + 1번까지 경기를 진행하며 참가자들의 승리 횟수를 카운팅한다.
    3. 2번에서 구한 승리 횟수 중 지우만 k를 만족하고 나머지는 k미만이면 1을 반환한다.
'''

import sys
from itertools import permutations
input = lambda: sys.stdin.readline().strip()

def solution(n, k, result, kyunghee, minho):
  answer = 0
  JIWOO, KYUNGHEE, MINHO = 0, 1, 2
  
  if n < k:
    return 0
  
  max_cnt = 3 * (k - 1) + 1
  for jw in permutations(range(1, n + 1), n):
    p1, p2 = JIWOO, KYUNGHEE
    game = [jw, kyunghee, minho]
    cur = [0, 0, 0]
    win = [0, 0, 0]
    for _ in range(max_cnt):
      next = [j for j in range(3) if j != p1 and j != p2][0] # 다음 상대를 선택
      x, y = game[p1][cur[p1]] - 1, game[p2][cur[p2]] - 1 # 현재 손동작을 찾음
      cur[p1] += 1
      cur[p2] += 1
      
      if result[x][y] == 2:
        p2 = next
        win[p1] += 1
      elif result[x][y] == 1:
        if p1 > p2:
          p2 = next
          win[p1] += 1
        else:
          p1 = next
          win[p2] += 1
      else:
        p1 = next
        win[p2] += 1
      
      if win[KYUNGHEE] >= k or win[MINHO] >=k:
        break
      elif win[JIWOO] >= k:
        return 1
      if win[JIWOO] + n - cur[JIWOO] < k: # 현재 이긴 횟수 + 남은 횟수가 k를 만족할 수 없을 때
        break
  
  return answer

if __name__ == '__main__':
  n, k = map(int, input().split())
  result = [list(map(int, input().split())) for _ in range(n)]
  kyunghee = list(map(int, input().split()))
  minho = list(map(int, input().split()))
  print(solution(n, k, result, kyunghee, minho))