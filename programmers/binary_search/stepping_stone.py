'''
  풀이
    구하고자 하는 것: n개의 바위를 제거했을 때 "징검다리 간격의 최소값 중 최대 길이"
    주어진 징검 다리 간격 최대 범위: 1 ~ 1,000,000,000
    1) 징검다리 간격의 범위를 볼 때 완전 탐색 불가능.
    2) 징검 다리 간격의 최소값을 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 0 ~ 도착지점(distance)까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 주어진 바위들간 간격이 해당값보다 작은 바위들을 순차적으로 제거하며 제거한 수를 구한다.
        (이때, 출발 지점은 0으로 놓고 도착 지점인 distance값을 고려해주어야 한다.)
      3. 2에서 제거한 수와 제거할 수를 비교해 다음 과정을 반복 수행하여 최대 간격을 구한다.
        3-1. 제거한 수 <= 제거할 수인 경우
          현재 간격이 너무 작기때문에 left = mid + 1로 간격을 늘리고 현재 중간값을 저장한다.
        3-2. 제거한 수 > 제거할 수인 경우
          현재 간격이 너무 크기때문에 right = mid - 1로 간격을 줄여준다.
'''

import sys

input = lambda: sys.stdin.readline().strip()

def solution(distance, rocks, n):
  rcks = sorted(rocks + [distance])
  def rm(target):
    cnt, prev = 0, 0
    for r in rcks:
      if r - prev < target:
        cnt += 1
      else:
        prev = r
    return cnt

  answer = -1
  left, right = 0, distance
  while left <= right:
    mid = (left + right) // 2
    if rm(mid) <= n:
      left = mid + 1
      answer = mid
    else:
      right = mid - 1

  return answer  
  
if __name__ == '__main__':
  d = 25
  r = [2, 14, 11, 21, 17]
  n = 2
  print(solution(d, r, n) == 4)