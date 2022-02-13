'''
  풀이
    구하고자 하는 것: M미터 이상 나무를 가져가기 위한 절단기 최대 높이
    주어진 나무 높이 최대 범위: 1 ~ 1,000,000,000
    1) 나무 높이 범위를 볼 때 완전 탐색 불가능.
    2) 절단기 설정 높이를 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 나무 높이(max(trees))까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 각 나무들을 잘랐을 때 잘린 나무들의 합을 구한다.
      3. 2에서 구한 잘린 나무들의 합과 가져가야 하는 최소 높이(m)을 비교해 다음 과정을 반복 수행하며 절단기의 최대 높이를 구한다.
        3-1. 잘린 나무들의 합 >= 가져가야 하는 최소 높이 
          절단기의 높이를 더 올릴 수 있으므로 left = mid + 1을 하고 현재 절단기의 높이를 저장한다.
        3-2. 잘린 나무들의 합 < 가져가야 하는 최소 높이
          나무들을 더 잘라야하므로 right = mid - 1로 절단기의 높이를 내린다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  _, m = map(int, input().split())
  trees = list(map(int, input().split()))
  cnt = lambda x: sum([t - x for t in trees if t - x > 0])

  answer = -1
  left, right = 0, max(trees)
  while left <= right:
    mid = (left + right) // 2
    if cnt(mid) < m:
      right = mid - 1
    else:
      left = mid + 1
      answer = mid
  print(answer)

if __name__ == '__main__':
  solution()