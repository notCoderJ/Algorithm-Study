'''
  어떤 리스트가 존재하고 해당 리스트 안에서 특정한 수(target)의 개수를 알아보자.
  
  이분 탐색에서 lower bound, upper bound를 이용하면 구할 수 있다!
  - lower bound: target이 처음 나오는 지점
  - upper bound: target을 처음 초과한 지점
  
  target이 없을 때 lower bound == upper bound
  target이 1개 일 때 upper bound - lower bound == 1
  target이 2개 이상일 때 upper bound - lower bound >= 2
  
  즉, upper bound - lower bound의 결과는 해당 리스트에서 target의 수를 의미한다.
'''

def get_target_count(list, target):
  def lower_bound():
    left, right = 0, len(list) - 1
    while left < right:
      mid = (left + right) // 2
      if list[mid] < target:
        left = mid + 1
      else:
        right = mid
    return left
      
  def upper_bound():
    left, right = 0, len(list) - 1
    while left < right:
      mid = (left + right) // 2
      if list[mid] <= target:
        left = mid + 1
      else:
        right = mid
    return left
  
  return upper_bound() - lower_bound()

# 파이썬 bisect 라이브러리 이용
from bisect import bisect_left, bisect_right

def get_target_count1(list, target):
  return bisect_right(list, target) - bisect_left(list, target)

if __name__ == '__main__':
  print(get_target_count([1,3,6,8,8,8,8,11,20], 8))
  print(get_target_count([1,3,6,8,8,8,8,11,20], 4))
  print(get_target_count([1,3,6,8,8,8,8,11,20], 1))
  
  print(get_target_count1([1,3,6,8,8,8,8,11,20], 8))
  print(get_target_count1([1,3,6,8,8,8,8,11,20], 4))
  print(get_target_count1([1,3,6,8,8,8,8,11,20], 1))