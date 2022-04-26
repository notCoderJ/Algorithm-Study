'''
  풀이
    전형적인 징검다리 유형 문제로 이분탐색의 Parametric Search를 사용하여 풀었다.
    
    1. 학생들이 점프하는 최소 거리를 이분 탐색의 대상으로 잡는다.
    2. 만약 n = 0이면 돌섬이 없으므로 탈출구까지 거리를 출력한다.
    3. 0부터 탈출구까지 거리 범위에서 이분 탐색을 반복 수행하며,
      각 중간값에 대해 모든 바위 간 간격이 중간값보다 크거나 같도록 바위들을 제거하고 제거한 수와 m을 비교한다.
      (주의할 점은 마지막 탈출구까지의 거리도 포함해줘야한다.)
      3-1. "제거 수 <= m"인 경우 아직 최소 점프 거리를 더 늘릴 수 있으므로 현재 거리를 answer에 저장하고 좌측값(left)을 mid + 1로 변경한다.
      3-2. "제거 수 > m"인 경우 최소 점프 거리를 더 줄여야하므로 우측값(right)를 mid - 1로 변경한다.
    4. answer를 출력한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(d, n, m, rocks):
  answer = 0
  MAX = d
  
  if n == 0:
    return d
  
  def remove(target):
    cnt = 0
    cur = 0
    for r in rocks + [MAX]:
      if r - cur < target:
        cnt += 1
      else:
        cur = r
    if cnt <= m:
      return True
    else:
      return False
      
  left, right = 0, MAX
  while left <= right:
    mid = (left + right) // 2
    if remove(mid):
      left = mid + 1
      answer = mid
    else:
      right = mid - 1
  
  return answer


if __name__ == '__main__':
  d, n, m = map(int, input().split())
  rocks = sorted([int(input()) for _ in range(n)])
  print(solution(d, n, m, rocks))