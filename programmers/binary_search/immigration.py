'''
  풀이
    구하고자 하는 것: n명이 심사받는 데 걸린 최소 시간
    주어진 심사 시간 최대 범위: 1 ~ 1,000,000,000
    1) 심사 시간 범위를 볼 때 완전 탐색 불가능.
    2) n명이 심사받는 데 걸린 시간을 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 심사 시간(max(심사시간들) * n)까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 각 심사관들이 처리하는 사람들 수의 합을 구한다.
      3. 2에서 구한 사람들 수와 총 입국자 수(n)를 비교해 다음 과정을 반복 수행하며 최소 시간을 구한다.
        3-1. 처리한 사람 수 >= 총 입국자 수
          처리 시간을 더 줄일 수 있으므로 right = mid - 1로 전체 처리 시간을 줄이고 현재 중간값을 저장한다.
        3-2. 처리한 사람 수 < 총 입국자 수
          처리 시간이 부족하므로 left = mid + 1로 전체 처리 시간을 늘려준다.
'''

def solution(n, times):
  answer = -1
  left, right = 1, max(times) * n
  cnt = lambda x: sum([x // t for t in times])
  
  while left <= right:
    mid = (left + right) // 2
    if cnt(mid) >= n:
      right = mid - 1
      answer = mid
    else:
      left = mid + 1
  return answer
  
if __name__ == "__main__":
  n = 6
  times = [7, 10]
  print(solution(n, times) == 28)