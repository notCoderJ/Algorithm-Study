'''
  풀이
    구하고자 하는 것: 징검 다리를 건널 수 있는 최대 인원
    주어진 디딤돌 숫자 최대 범위: 1 ~ 2,000,000,000
    1) 디딤돌 숫자 범위를 볼 때 완전 탐색 불가능.
    2) 징검 다리를 건널 수 있는 인원을 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 디딤돌 숫자(max(stones))까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 건너뛸 수 있는 거리 중 최댓값을 구한다.(이때, 출발 위치와 도착 위치를 고려해주어야 한다)
        출발 위치 인덱스 -1, 도착 위치 값 2,000,000,000으로 설정하여 최대 인원을 수용하도록 설정.
      3. 2에서 구한 건너뛸 수 있는 거리와 가능한 건너뛸 수 있는 거리(k)를 비교해 다음 과정을 반복 수행하며 최대 인원을 구한다.
        3-1. 건너뛸 수 있는 거리 > 가능한 건너뛸 수 있는 거리(k)
          징검다리를 건널 수 있는 인원을 더 줄여야 하므로 right = mid - 1로 건널 인원을 줄인다.
        3-2. 건너뛸 수 있는 거리 <= 가능한 건너뛸 수 있는 거리(k)
          징검다리를 건널 수 있는 인원을 더 늘려도 되므로 left = mid + 1로 건널 인원을 늘리고 현재 건널 인원을 저장한다.
'''

import sys

input = lambda: sys.stdin.readline().strip()

def solution(stones, k):
  def space(target):
    width, prev = -1, -1
    for i, s in enumerate(stones + [200000000]):
      if s - target < 0:
        continue
      width = max(width, i - prev)
      prev = i
    return width
  
  answer = 0
  left, right = 1, max(stones)
  while left <= right:
    mid = (left + right) // 2
    if space(mid) > k:
      right = mid - 1
    else:
      left = mid + 1
      answer = mid
  
  return answer

if __name__ == "__main__":
  stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
  k = 3
  print(solution(stones, k) == 3)