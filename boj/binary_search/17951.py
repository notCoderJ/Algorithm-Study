'''
  풀이
    13397번 문제와 비슷한 유형의 문제였고 마찬가지로 이분 탐색을 사용하여 풀이하였다.
    그룹별 맞은 개수의 합 중 최솟값을 이분 탐색 대상으로 잡고 Parametric Search를 적용하면 된다.
    먼저, 중간 값에 대해 그룹핑을 진행할 함수를 다음과 같이 정의해주었다.
    맞은 개수를 순서대로 누적하면서
      1. "누적 맞은 개수 < 현재 중간 값"이면 아직 그룹 점수가 부족하므로 동일 그룹에 점수를 더 추가한다.
      2. "누적 맞은 개수 >= 현재 중간 값"이면 새로운 그룹을 하나 추가하고 누적 점수를 초기화한다.
    위 과정이 끝나면 생성한 그룹 수를 반환한다.
    (이때, 주의할 점은 마지막 누적 점수가 현재 중간값보다 적은 경우 마지막 그룹을 제외한 그룹 수를 반환해야 한다.)
    
    만약 반환된 그룹 수 >= k이면 그룹별 점수를 더 높여도 되므로 현재 중간 값을 기록하고 좌측 포인터를 중간값 + 1로 변경한다.
    그렇지 않으면 그룹별 점수를 더 낮춰야되므로 우측 포인터를 중간값 - 1로 변경한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, k = map(int, input().split())
  scores = list(map(int, input().split()))
  
  def grouping(target):
    cnt, cur = 1, 0
    for s in scores:
      if cur < target:
        cur += s
      else:
        cnt += 1
        cur = s
    return cnt if cur >= target else cnt - 1

  left, right = 0, n * 20
  while left <= right:
    mid = (left + right) // 2
    if grouping(mid) >= k:
      answer = mid
      left = mid + 1
    else:
      right = mid - 1
  
  print(answer)
  
if __name__ == '__main__':
  solution()