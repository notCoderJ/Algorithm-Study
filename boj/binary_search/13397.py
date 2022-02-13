'''
  풀이
    처음에는 구간 당 m개 이하라는 건지 전체를 m개의 구간 이하로 쪼개라는 건지 제대로 이해가 안되서 한참 헤맸다.
    구간 분리를 이해하고도 어떻게 쪼개야할지 방법이 잘 떠오르지 않았다...
    아니 떠오르긴 했지만 잘못 생각한 부분이 있어 그 방법이 맞다는 게 검증이 안되서 한참 고민했다.
    (구간에 하나의 원소만 존재할 경우 점수가 0이 된다는 걸 잘못생각하고 있었다;)

    주어진 범위에서 구간을 쪼개는 경우의 수가 상당히 많기 때문에 완전 탐색으로는 불가능하다고 생각했고
    구간 점수의 최댓값을 이분 탐색의 대상으로 잡고 Parametric Search를 적용하였다.
    중간 값에 대해 해당 값 이하를 점수로 하는 구간들로 나눈 후 구간의 수가 m개 이하인지 확인하였는데,
    이때, 주어진 수들을 순회하며 각 자리에서 구한 점수가 중간 값보다 작거나 같으면 같은 구간에 넣고 크면 새로운 구간을 생성하도록 하였다.
    위 과정을 반복하며 가능한 최댓값의 범위를 좁혀 구간 점수의 최댓값의 최솟값을 구하였다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  
  def group(target):
    cnt = 1
    _min, _max = 10001, 0
    for num in nums:
      _min = min(_min, num)
      _max = max(_max, num)
      if _max - _min > target:
        cnt += 1
        _min, _max = num, num
    return True if cnt <= m else False

  left, right = 0, 9999
  while left <= right:
    mid = (left + right) // 2
    if group(mid):
      answer = mid
      right = mid -1
    else:
      left = mid + 1

  print(answer)
  
if __name__ == '__main__':
  solution()