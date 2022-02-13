'''
  풀이
    구하고자 하는 것: 전체 심사받는 데 걸리는 최소 시간
    주어진 심사 시간의 최대 범위: 1 ~ 1,000,000,000
    상근이 + 친구들 최대 범위: 1 ~ 1,000,000,000
    1) 심사 시간 * 인원의 범위를 볼 때 완전 탐색 불가능.
    2) 총 심사 시간을 이분탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 전체 심사 시간(max(심사시간) * 인원)까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 각 심사관이 심사할 수 있는 인원의 합을 구한다.
      3. 2에서 구한 심사한 총 인원과 심사해야하는 총 인원(m)를 비교해 다음 과정을 반복 수행하며 전체 심사 시간을 구한다.
        3-1. 심사한 총 인원 < 심사해야하는 총 인원
          전체 심사 시간이 더 걸리므로 left = mid + 1로 전체 심사 시간을 늘린다.
        3-2. 심사한 총 인원 >= 심사해야하는 총 인원
          전체 심사 시간이 더 적게 걸리므로 right = mid - 1로 전체 심사 시간을 줄이고 현재 심사 시간을 저장한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, m = map(int, input().split())
  delays = [int(input()) for _ in range(n)]
  cnt = lambda x: sum([x // d for d in delays])
  
  left, right = 1, max(delays) * m
  while left <= right:
    mid = (left + right) // 2
    if cnt(mid) < m:
      left = mid + 1
    else:
      right = mid - 1
      answer = mid

  print(answer)

if __name__ == "__main__":
  solution()